from unittest.mock import MagicMock, patch
from infrastructure.repositories.funcionarioRepository import FuncioarioRepository
from infrastructure.models.funcionarioModel import FuncionarioModel
from domain.values_objects.paginator import Pagination
from tests.factories.funcionario_factory import funcionario_model_valido

def test_buscar_por_email_quando_encontrar(db_session_mock):
    funcionario_db = funcionario_model_valido(
        email_corporativo="teste@empresa.com"
    )

    db_session_mock.query.return_value.where.return_value.first.return_value = funcionario_db

    repo = FuncioarioRepository(db_session_mock)

    result = repo.buscar_por_email("teste@empresa.com")

    assert result["email_corporativo"] == "teste@empresa.com"
    


def test_buscar_pagina(db_session_mock):
    funcionario1 = funcionario_model_valido(id=1)
    funcionario2 = funcionario_model_valido(id=2)

    db_session_mock.query.return_value.offset.return_value.limit.return_value.all.return_value = [
        funcionario1,
        funcionario2
    ]

    repo = FuncioarioRepository(db_session_mock)
    pagination = Pagination(page=1, size=2)

    result = repo.buscar_pagina(pagination)

    assert len(result) == 2


def test_criar_analise_enps(db_session_mock):
    """
    Deve calcular corretamente o eNPS a partir dos valores retornados do banco,
    delegando o cálculo para o objeto Analise.
    """
    db_session_mock.query.return_value.all.return_value = [
        (10,),
        (9,),
        (2,)
    ]

    repo = FuncioarioRepository(db_session_mock)

    with patch.object(repo, "_FuncioarioRepository__analise") as analise_mock:
        analise_mock.calcular_enps.return_value = 33

        result = repo.criar_analise_enps()

        assert result == 33
        analise_mock.calcular_enps.assert_called_once()


def test_criar_analise_likert(db_session_mock):
    """
    Deve calcular a distribuição percentual Likert (1 a 5)
    para cada coluna analisada com base nos dados do banco.
    """
    db_session_mock.query.return_value.all.return_value = [
        (7, 6, 5, 4, 3, 2, 1),
        (6, 6, 5, 5, 3, 2, 1)
    ]

    repo = FuncioarioRepository(db_session_mock)

    with patch.object(repo, "_FuncioarioRepository__analise") as analise_mock:
        analise_mock.calcular_likert.side_effect = lambda v: 5 if v >= 6 else 3

        result = repo.criar_analise_likert()

        assert "interesse_no_cargo" in result
        assert "likert_pct" in result["interesse_no_cargo"]
        assert "total_respostas" in result["interesse_no_cargo"]


def test_criar_analise_favorabilidade(db_session_mock):
    """
    Deve calcular a favorabilidade (favorável, neutro, desfavorável)
    para cada dimensão analisada, retornando os percentuais corretamente.
    """
    db_session_mock.query.return_value.all.return_value = [
        (7, 6, 5, 4, 3, 2, 1),
        (6, 6, 5, 5, 3, 2, 1)
    ]

    repo = FuncioarioRepository(db_session_mock)

    with patch.object(repo, "_FuncioarioRepository__analise") as analise_mock:
        analise_mock.calcular_likert.side_effect = lambda v: 5 if v >= 6 else 3
        analise_mock.calcular_favorabilidade.return_value = {
            "favoravel_pct": 4,
            "neutro_pct": 2,
            "desfavoravel_pct": 0
        }

        result = repo.criar_analise_favorabilidade()

        assert "interesse_no_cargo" in result
        assert "favorabilidade" in result["interesse_no_cargo"]

        favorabilidade = result["interesse_no_cargo"]["favorabilidade"]

        assert "favoravel" in favorabilidade
        assert "neutro" in favorabilidade
        assert "desfavoravel" in favorabilidade
