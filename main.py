from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from modelos.smart import Smart
from modelos.usuarios import Usuarios
from modelos.banco import MongoDBClient
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# --------------
#   Informações do banco
#
load_dotenv(dotenv_path='config/banco.env')
uri = os.getenv('URI')
database_name = os.getenv('DATABASE_NAME')

# --------------
#   instancio o banco
#
mongo_client = MongoDBClient(str(uri), str(database_name))

# --------------
#   Instancia FastAPI
#
app = FastAPI()

# --------------
#   /
#
@app.get("/")
def hello_world():
    return {"Hello": "World"}

# --------------
#   Inseri um usuario
#
@app.post("/usuarios/criar_usuario/")
def criar_usuario(nome: str, sobrenome: str):

    usuario = Usuarios(nome, sobrenome, mongo_client)
    result = usuario.save_to_db()

    if 'Erro' in result:
        return JSONResponse(result, status_code=400)
    else:
        mensagem = {'Token': usuario.get_token()}
        return JSONResponse(mensagem, status_code=200)