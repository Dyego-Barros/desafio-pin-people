from fastapi import APIRouter,Depends
from application.services.funcionario_service import FuncionarioService
from core.database import Database
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import status
import json
#Cria instância do banco
database = Database()

routers= APIRouter(prefix='/funcionario', tags=['Funcionario'])


@routers.post('/buscar/email')
def listar(email:str, db : Session = Depends(database.get_connection)):
    service = FuncionarioService(db=db)
    try:
        func = service.buscar_email(email=email)
        if func:
            return JSONResponse(content={"Dados":func}, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"Dados":"Nenhum dado encontrado referente a este e-mail!"}, status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content={"Error":"A api se comportour de forma inesperada, por favor tente novamente."}, status_code=status.HTTP_404_NOT_FOUND)
    
@routers.get("/pagina")
def busca_pagina(page:int,size:int, db:Session=Depends(database.get_connection)):
    service = FuncionarioService(db=db)
    try:
        dados = service.buscar_pagina(page=page,size=size)
        if dados:
            return JSONResponse(content={"page":page,"size":size,"dados":dados}, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"page":page,"size":size,"dados":"Nenhum dado encontrado na pagina fornecida"}, status_code=status.HTTP_200_OK)
    except Exception as error:        
        return JSONResponse(content={"Error":"A api se comportour de forma inesperada, por favor tente novamente."}, status_code=status.HTTP_404_NOT_FOUND)
    
@routers.get("/analise/likert")
def analise_likert(db: Session=Depends(database.get_connection)):
    service = FuncionarioService(db=db)
    try:
        dados = service.analise_likert()
        if dados:
             return JSONResponse(content={"likert":dados}, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"likert":"Não conseguimos processar seu pedido de relatorio"}, status_code=status.HTTP_200_OK)
        
    except Exception as error:
        return JSONResponse(content={"Error":"A api se comportour de forma inesperada, por favor tente novamente."}, status_code=status.HTTP_404_NOT_FOUND)
    
@routers.get("/analise/favorabilidade")
def analise_favorabilidade(db: Session=Depends(database.get_connection)):
    service = FuncionarioService(db=db)
    try:
        dados = service.analise_favorabilidade()
        if dados:
            return JSONResponse(content={"favorabilidade":dados}, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"favorabilidade":"Não conseguimos processar seu pedido de relatorio"}, status_code=status.HTTP_200_OK)        
    except Exception as error:
        return JSONResponse(content={"Error":"A api se comportour de forma inesperada, por favor tente novamente."}, status_code=status.HTTP_404_NOT_FOUND)
    
        
@routers.get("/analise/enps")
def analise_enps(db: Session=Depends(database.get_connection)):
    service = FuncionarioService(db=db)
    try:
        dados = service.analise_enps()
        if dados:
            return JSONResponse(content={"enps":dados}, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"enps":"Não conseguimos processar seu pedido de relatorio"}, status_code=status.HTTP_200_OK)        
    except Exception as error:
        return JSONResponse(content={"Error":"A api se comportour de forma inesperada, por favor tente novamente."}, status_code=status.HTTP_404_NOT_FOUND)
    