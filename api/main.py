from fastapi import FastAPI
from interface.routes.funcionario_router import routers

app = FastAPI(title="Desafio Pin People", version="0.1.0", description="Api do teste técnico da Pin People")

app.include_router(router= routers)

if __name__=="__main__":
    import uvicorn as uv
    uv.run("main:app", host="0.0.0.0", port=8000,reload=True)