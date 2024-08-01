from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from modelos.banco import MongoDBClient
from dotenv import load_dotenv
from datetime import datetime
from bson import ObjectId
import os
from typing import Dict, Any

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

@router.post("/smart/", tags=["smart"])
async def post_smart(document: Dict[str, Any]):
    """Cria novo smart"""

    document_dict = document.copy()
    document_dict.update({
        "criado_em": datetime.now(),
        "atualizado_em": datetime.now(),
        "deletado": False
        })

    result = mongo_client.insert_document("smart", document_dict)

    if 'Erro' in result:
        return JSONResponse(result, status_code=400)
    else:
        user_id = result['_id']
        mensagem = {'id': str(user_id)}
        return JSONResponse(mensagem, status_code=200)
    
@router.get("/smart/id/{id}", tags=["smart"])
async def get_smart_by_id(id: str):
    """busca um smart pelo id"""
    obj = mongo_client.find_one_document("smart", {"_id": ObjectId(str(id))})

    if obj is None:
        return JSONResponse({"mensage": "Smart não encontrado"}, status_code=404)
    elif 'Erro' in obj:
        return JSONResponse(obj, status_code=400)
    else:
        result = {
            "id": str(obj["_id"]),
            "usuario_id": obj["usuario_id"],
            "especifica": obj["especifica"],
            "mensuravel": obj["mensuravel"],
            "atingivel": obj["atingivel"],
            "relevante": obj["relevante"],
            "temporizavel": obj["temporizavel"],
            "status": obj["status"],
            "criado_em": str(obj["criado_em"]),
            "atualizado_em": str(obj["atualizado_em"]),
            "deletado": obj["deletado"]
        }

        return JSONResponse(result, status_code=200)

@router.get("/smart/usuario/{usuario_id}", tags=["smart"])
async def get_smart_by_usuario_id(usuario_id: str):
    """busca uma lista de smarts pelo usuario_id"""
    response = mongo_client.find_document("smart", {"usuario_id": str(usuario_id)})
    list_objs = []

    for obj in response:
        result = {
            "id": str(obj["_id"]),
            "usuario_id": obj["usuario_id"],
            "especifica": obj["especifica"],
            "mensuravel": obj["mensuravel"],
            "atingivel": obj["atingivel"],
            "relevante": obj["relevante"],
            "temporizavel": obj["temporizavel"],
            "status": obj["status"],
            "criado_em": str(obj["criado_em"]),
            "atualizado_em": str(obj["atualizado_em"]),
            "deletado": obj["deletado"]
        }
        list_objs.append(result)

    return JSONResponse(list_objs, status_code=200)

@router.get("/smart/", tags=["smart"])
async def get_list_smart():
    """lista os smarts"""
    result = mongo_client.find_document("smart", None)

    list_users = []
    for obj in result:
        result = {
            "id": str(obj["_id"]),
            "usuario_id": obj["usuario_id"],
            "especifica": obj["especifica"],
            "mensuravel": obj["mensuravel"],
            "atingivel": obj["atingivel"],
            "relevante": obj["relevante"],
            "temporizavel": obj["temporizavel"],
            "status": obj["status"],
            "criado_em": str(obj["criado_em"]),
            "atualizado_em": str(obj["atualizado_em"]),
            "deletado": obj["deletado"]
        }
        list_users.append(result)
    return JSONResponse(list_users, status_code=200)