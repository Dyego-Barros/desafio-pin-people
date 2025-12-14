from abc import ABC, abstractmethod
from domain.entities.funcionario_entitie import Funcionario
from domain.values_objects.paginator import Pagination

class Ifuncionario:
    
  
    @abstractmethod
    def criar_analise_likert(self)->list[dict]:
        raise NotImplementedError
        
    @abstractmethod
    def criar_analise_enps(self)-> list[dict]:
        raise NotImplementedError
    
    @abstractmethod
    def criar_analise_favorabilidade(self)->list[dict]:
        raise NotImplementedError
    
    @abstractmethod
    def buscar_por_email(self, email:str)->Funcionario:
        raise NotImplementedError
    
    @abstractmethod
    def buscar_pagina(self, pagination:Pagination)-> list[Funcionario]:
        raise NotImplementedError