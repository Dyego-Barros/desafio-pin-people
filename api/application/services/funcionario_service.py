from infrastructure.repositories.funcionarioRepository import FuncioarioRepository
import logging
from domain.values_objects.paginator import Pagination
from sqlalchemy.orm import Session
logger = logging.getLogger(__name__)



class FuncionarioService():
    def __init__(self, db: Session):
        self.__repo = FuncioarioRepository(db=db)
        
      
    def buscar_email(self, email:str):
        try:
            user = self.__repo.buscar_por_email(email=email)
            if user:
                return user
            return None
        except Exception as error:
            logger.error(error)
            return None
    def buscar_pagina(self,page:int,size:int):
        try:
            paginator = Pagination(page=page, size=size)
            dados = self.__repo.buscar_pagina(pagination=paginator)
            if dados:
                return dados
            return None
        except Exception as error:
            logger.error(error)
            return None
        
    def analise_likert(self):
        try:
            
            dados = self.__repo.criar_analise_likert()
            if dados:
                return dados
            return None
        except Exception as error:
            logger.error(error)
            return None
    
    def analise_favorabilidade(self):
        try:            
            dados = self.__repo.criar_analise_favorabilidade()
            if dados:
                return dados
            return None      
        except Exception as error:
            logger.error(error)
            raise error
        
    def analise_enps(self):
        try:
            
            dados = self.__repo.criar_analise_enps()
            if dados:
                return dados
            return None
        except Exception as error:
            logger.error(error)
            raise error