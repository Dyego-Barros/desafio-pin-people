import pandas as pd 
from sqlalchemy import create_engine, text
import os

#PEga o path absoluto
FILE_PATH = os.path.abspath(os.path.dirname(os.path.join(os.path.abspath(__file__))))

#Le o csv e carrega os dados na memoria
data = pd.read_csv(f"{FILE_PATH}/data.csv", sep=";", engine="python")

#Cria a engine de conexão com banco para ingestão dos dados
engine = create_engine('postgresql+psycopg2://admin:admin123@127.0.0.1:5432/desafio')

#Insere os dados no banco
data.to_sql('desafio',engine,if_exists='replace',index=False )

with engine.connect() as conn:
   
    conn.execute(text("""
                 ALTER TABLE desafio
                 ADD COLUMN id SERIAL PRIMARY KEY
                 """))
    conn.execute(text("""CREATE UNIQUE INDEX idx_email on desafio(email);"""))
    conn.execute(text(""" CREATE UNIQUE INDEX idx_email_corporativo on desafio(email_corporativo);"""))
    conn.execute(text("""CREATE INDEX idx_data_resposta on desafio (data_da_resposta);"""))
    conn.commit()
    conn.close()