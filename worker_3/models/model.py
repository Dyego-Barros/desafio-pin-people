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
    
    
    