from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from modelos.banco import MongoDBClient
from dotenv import load_dotenv
from datetime import datetime
from bson import ObjectId
import os

router = APIRouter()

# --------------
#   configs
load_dotenv(dotenv_path='config/config.env')
uri = os.getenv('URI')
database_name = os.getenv('DATABASE_NAME')
api_version = os.getenv('API_VERSION')

# --------------
#   instancia o banco
mongo_client = MongoDBClient(str(uri), str(database_name))

@router.post("/usuarios/", tags=["usuarios"])
async def post_usuario(nome: str, sobrenome: str):
    """Cria novo usuário"""
    document = {
        "nome": nome,
        "sobrenome": sobrenome,
        "criado_em": datetime.now(),
        "atualizado_em": datetime.now(),
        "deletado": False
    }

    result = mongo_client.insert_document("usuarios", document)

    if 'Erro' in result:
        return JSONResponse(result, status_code=400)
    else:
        user_id = result['_id']
        mensagem = {'id': str(user_id)}
        return JSONResponse(mensagem, status_code=200)
    
@router.get("/usuarios/{id}", tags=["usuarios"])
async def get_usuario(id: str):
    """busca um usuário"""
    obj = mongo_client.find_one_document("usuarios", {"_id": ObjectId(str(id))})

    result = {
        "id": str(obj["_id"]),
        "nome": obj["nome"],
        "sobrenome": obj["sobrenome"],
        "criado_em": str(obj["criado_em"]),
        "atualizado_em": str(obj["atualizado_em"]),
        "deletado": obj["deletado"]
    }

    if 'Erro' in obj:
        return JSONResponse(obj, status_code=400)
    else:
        return JSONResponse(result, status_code=200)

@router.get("/usuarios/", tags=["usuarios"])
async def get_list_usuario():
    """lista os usuários"""
    result = mongo_client.find_document("usuarios", None)

    list_users = []
    for obj in result:
        print(obj)
        result = {
            "id": str(obj["_id"]),
            "nome": obj["nome"],
            "sobrenome": obj["sobrenome"],
            "criado_em": str(obj["criado_em"]),
            "atualizado_em": str(obj["atualizado_em"]),
            "deletado": obj["deletado"]
        }
        list_users.append(result)
    return JSONResponse(list_users, status_code=200)


