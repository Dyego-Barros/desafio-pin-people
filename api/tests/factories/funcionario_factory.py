from infrastructure.models.funcionarioModel import FuncionarioModel

def funcionario_model_valido(**overrides):
    dados = {
        "id": 1,
        "nome": "João Silva",
        "email": "joao@empresa.com",
        "email_corporativo": "joao@empresa.com",
        "area": "TI",
        "cargo": "Dev",
        "funcao": "Backend",
        "localidade": "SP",
        "tempo_de_empresa": "2 anos",
        "genero": "M",
        "geracao": "Y",
        "n0_empresa": "Empresa",
        "n1_diretoria": "Diretoria",
        "n2_gerencia": "Gerencia",
        "n3_coordenacao": "Coord",
        "n4_area": "Area",
        "data_da_resposta": "2024-01-01",
        "comentarios_interesse_no_cargo": "",
        "comentarios_contribuicao": "",
        "comentarios_aprendizado_e_desenvolvimento": "",
        "comentarios_feedback": "",
        "comentarios_interacao_com_gestor": "",
        "comentarios_clareza_sobre_possibilidades_de_carreira": "",
        "comentarios_expectativa_de_permanencia": "",
        "aberta_enps": "",
    }

    dados.update(overrides)
    return FuncionarioModel(**dados)
