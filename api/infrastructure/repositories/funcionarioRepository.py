from domain.interfaces.Ifuncionario import Ifuncionario
from domain.entities.funcionario_entitie import Funcionario
from sqlalchemy.orm import Session
from infrastructure.models.funcionarioModel import FuncionarioModel
from domain.values_objects.paginator import Pagination
from domain.values_objects.analise import Analise


class FuncioarioRepository(Ifuncionario):
    #Injeta dependencia
    def __init__(self, db: Session):
        self.__db = db            
        self.__analise=Analise()  
        
    def buscar_por_email(self, email:str)-> Funcionario:
        try:
            user = self.__db.query(FuncionarioModel).where(FuncionarioModel.email_corporativo==email).first()
            if user:                
                return Funcionario.model_validate(user).model_dump()
        except Exception as error:
            raise error
        
    def buscar_pagina(self, pagination: Pagination) ->list[Funcionario]:
        try:
           dados = self.__db.query(FuncionarioModel).offset(pagination.offset).limit(pagination.size).all()
           
           if dados:
                lista_dados =[Funcionario.model_validate(dado).model_dump() for dado in dados] 
                return lista_dados        
           return []
        except Exception as error:
            raise error
        
    def criar_analise_likert(self) -> dict:
        try:
            campos = [
                FuncionarioModel.interesse_no_cargo,
                FuncionarioModel.contribuicao,
                FuncionarioModel.aprendizado_e_desenvolvimento,
                FuncionarioModel.feedback,
                FuncionarioModel.interacao_com_gestor,
                FuncionarioModel.clareza_sobre_possibilidades_de_carreira,
                FuncionarioModel.expectativa_de_permanencia
            ]

            dados = self.__db.query(*campos).all()

            colunas = {
                "interesse_no_cargo": [],
                "contribuicao": [],
                "aprendizado_e_desenvolvimento": [],
                "feedback": [],
                "interacao_com_gestor": [],
                "clareza_sobre_possibilidades_de_carreira": [],
                "expectativa_de_permanencia": [],
            }

            # separa valores coluna a coluna
            for row in dados:
                colunas["interesse_no_cargo"].append(row[0])
                colunas["contribuicao"].append(row[1])
                colunas["aprendizado_e_desenvolvimento"].append(row[2])
                colunas["feedback"].append(row[3])
                colunas["interacao_com_gestor"].append(row[4])
                colunas["clareza_sobre_possibilidades_de_carreira"].append(row[5])
                colunas["expectativa_de_permanencia"].append(row[6])

            resultado_final = {}

            for coluna, valores in colunas.items():
                # convertendo notas 1-7 para likert 1-5
                likerts = [self.__analise.calcular_likert(v) for v in valores]

                # remove None (caso existam)
                likerts_validos = [v for v in likerts if v is not None]
                total = len(likerts_validos)

                # evita divisão por zero
                if total == 0:
                    pct = {str(i): 0 for i in range(1, 6)}
                else:
                    pct = {
                        "1": round((likerts_validos.count(1) / total) * 100, 2),
                        "2": round((likerts_validos.count(2) / total) * 100, 2),
                        "3": round((likerts_validos.count(3) / total) * 100, 2),
                        "4": round((likerts_validos.count(4) / total) * 100, 2),
                        "5": round((likerts_validos.count(5) / total) * 100, 2)
                    }

                resultado_final[coluna] = {
                    "likert_pct": pct,
                    "total_respostas": total
                }

            return resultado_final

        except Exception as error:
            raise error

        
    def criar_analise_enps(self)->bool:
        try:
            
            campos=[
                FuncionarioModel.enps
            ]
            dados = self.__db.query(*campos).all()
            
            results = [{"enps":dado[0]} for dado in dados]
          
            enps = self.__analise.calcular_enps(results)
                
              
            
            return enps
            
        except Exception as error:
            raise error
    
    def criar_analise_favorabilidade(self):
        try:
            campos = [
                FuncionarioModel.interesse_no_cargo,
                FuncionarioModel.contribuicao,
                FuncionarioModel.aprendizado_e_desenvolvimento,
                FuncionarioModel.feedback,
                FuncionarioModel.interacao_com_gestor,
                FuncionarioModel.clareza_sobre_possibilidades_de_carreira,
                FuncionarioModel.expectativa_de_permanencia
            ]
            
            dados = self.__db.query(*campos).all()
            
            colunas = {
                "interesse_no_cargo": [],
                "contribuicao": [],
                "aprendizado_e_desenvolvimento": [],
                "feedback": [],
                "interacao_com_gestor": [],
                "clareza_sobre_possibilidades_de_carreira": [],
                "expectativa_de_permanencia": [],
            }
            
            for row in dados:
                colunas["interesse_no_cargo"].append(row[0])
                colunas["contribuicao"].append(row[1])
                colunas["aprendizado_e_desenvolvimento"].append(row[2])
                colunas["feedback"].append(row[3])
                colunas["interacao_com_gestor"].append(row[4])
                colunas["clareza_sobre_possibilidades_de_carreira"].append(row[5])
                colunas["expectativa_de_permanencia"].append(row[6])
            
            resultado_final = {}
            
            for coluna, valores in colunas.items():
                # converte os valores para likert usando sua função
                likerts = [self.__analise.calcular_likert(v) for v in valores]

                # calcula alegria/neutral/desfavorável
                fav = self.__analise.calcular_favorabilidade(likerts)

                total = len(likerts)

                # converte para porcentagem
                fav_percentual = {
                    "favoravel": round((fav["favoravel_pct"] / total) * 100, 2) if total else 0,
                    "neutro": round((fav["neutro_pct"] / total) * 100, 2) if total else 0,
                    "desfavoravel": round((fav["desfavoravel_pct"] / total) * 100, 2) if total else 0,
                }
                
                resultado_final[coluna] = {
                    "favorabilidade": fav_percentual
                }
            
            return resultado_final
        
        except Exception as error:
            raise error

        
        