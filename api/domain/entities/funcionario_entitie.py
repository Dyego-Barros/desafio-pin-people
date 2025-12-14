# Entidade de dominio de Funcionario
from pydantic import BaseModel, EmailStr
from typing import Optional

class Funcionario(BaseModel):
    id: Optional[int]
    nome: str
    email: EmailStr
    email_corporativo: Optional[EmailStr]
    area: str
    cargo: str
    funcao: Optional[str]
    localidade: Optional[str]
    tempo_de_empresa: Optional[str]
    genero: Optional[str]
    geracao: Optional[str]
    n0_empresa: Optional[str]
    n1_diretoria: Optional[str]
    n2_gerencia: Optional[str]
    n3_coordenacao: Optional[str]
    n4_area: Optional[str]
    data_da_resposta: Optional[str]
    interesse_no_cargo: Optional[int]
    comentarios_interesse_no_cargo: Optional[str]
    contribuicao: Optional[int]
    comentarios_contribuicao: Optional[str]
    aprendizado_e_desenvolvimento: Optional[int]
    comentarios_aprendizado_e_desenvolvimento: Optional[str]
    feedback: Optional[int]
    comentarios_feedback: Optional[str]
    interacao_com_gestor: Optional[int]
    comentarios_interacao_com_gestor: Optional[str]
    clareza_sobre_possibilidades_de_carreira: Optional[int]
    comentarios_clareza_sobre_possibilidades_de_carreira: Optional[str]
    expectativa_de_permanencia: Optional[int]
    comentarios_expectativa_de_permanencia: Optional[str]
    enps: Optional[int]
    aberta_enps: Optional[str]
    
    model_config={
        "from_attributes": True
    }
