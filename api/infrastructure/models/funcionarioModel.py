# app/infrastructure/models/funcionario_model.py
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FuncionarioModel(Base):
    __tablename__ = "desafio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    email_corporativo = Column(String(255), unique=True)
    area = Column(String(255), nullable=False)
    cargo = Column(String(255), nullable=False)
    funcao = Column(String(255))
    localidade = Column(String(255))
    tempo_de_empresa = Column(String)
    genero = Column(String(50))
    geracao = Column(String(50))
    n0_empresa = Column(String(255))
    n1_diretoria = Column(String(255))
    n2_gerencia = Column(String(255))
    n3_coordenacao = Column(String(255))
    n4_area = Column(String(255))
    data_da_resposta = Column(String(50))  # ou Date, se for formatado como YYYY-MM-DD
    interesse_no_cargo = Column(Integer)
    comentarios_interesse_no_cargo = Column(Text)
    contribuicao = Column(Integer)
    comentarios_contribuicao = Column(Text)
    aprendizado_e_desenvolvimento = Column(Integer)
    comentarios_aprendizado_e_desenvolvimento = Column(Text)
    feedback = Column(Integer)
    comentarios_feedback = Column(Text)
    interacao_com_gestor = Column(Integer)
    comentarios_interacao_com_gestor = Column(Text)
    clareza_sobre_possibilidades_de_carreira = Column(Integer)
    comentarios_clareza_sobre_possibilidades_de_carreira = Column(Text)
    expectativa_de_permanencia = Column(Integer)
    comentarios_expectativa_de_permanencia = Column(Text)
    enps = Column(Integer)
    aberta_enps = Column(Text)
    
    
    def to_dict(self) -> dict:
        """
        Retorna um dicionário com todos os campos da instância.
        """
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "email_corporativo": self.email_corporativo,
            "area": self.area,
            "cargo": self.cargo,
            "funcao": self.funcao,
            "localidade": self.localidade,
            "tempo_de_empresa": self.tempo_de_empresa,
            "genero": self.genero,
            "geracao": self.geracao,
            "n0_empresa": self.n0_empresa,
            "n1_diretoria": self.n1_diretoria,
            "n2_gerencia": self.n2_gerencia,
            "n3_coordenacao": self.n3_coordenacao,
            "n4_area": self.n4_area,
            "data_da_resposta": self.data_da_resposta,
            "interesse_no_cargo": self.interesse_no_cargo,
            "comentarios_interesse_no_cargo": self.comentarios_interesse_no_cargo,
            "contribuicao": self.contribuicao,
            "comentarios_contribuicao": self.comentarios_contribuicao,
            "aprendizado_e_desenvolvimento": self.aprendizado_e_desenvolvimento,
            "comentarios_aprendizado_e_desenvolvimento": self.comentarios_aprendizado_e_desenvolvimento,
            "feedback": self.feedback,
            "comentarios_feedback": self.comentarios_feedback,
            "interacao_com_gestor": self.interacao_com_gestor,
            "comentarios_interacao_com_gestor": self.comentarios_interacao_com_gestor,
            "clareza_sobre_possibilidades_de_carreira": self.clareza_sobre_possibilidades_de_carreira,
            "comentarios_clareza_sobre_possibilidades_de_carreira": self.comentarios_clareza_sobre_possibilidades_de_carreira,
            "expectativa_de_permanencia": self.expectativa_de_permanencia,
            "comentarios_expectativa_de_permanencia": self.comentarios_expectativa_de_permanencia,
            "enps": self.enps,
            "aberta_enps": self.aberta_enps
        }