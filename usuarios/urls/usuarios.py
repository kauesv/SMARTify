from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.banco import MongoDBClient
from datetime import datetime
from bson import ObjectId
from typing import Dict, Any
from config import Config


# --------------
#   configs
uri = Config.BANCO_URI
database_name = Config.DATABASE_NAME

# --------------
#   instancia o banco
mongo_client = MongoDBClient(str(uri), str(database_name))

# --------------
#   
router = APIRouter()

# --------------
#   
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

# --------------
#   
@router.get("/usuarios/id/{id}", tags=["usuarios"])
async def get_usuario_by_id(id: str):
    """busca um usuário"""
    obj = mongo_client.find_one_document("usuarios", {"_id": ObjectId(str(id))})

    if obj:
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
    else:
        return JSONResponse({"Message": "ID não encontrado"}, status_code=404)

# --------------
#   
@router.get("/usuarios/", tags=["usuarios"])
async def get_list_usuario():
    """lista os usuários"""
    result = mongo_client.find_document("usuarios", None)

    list_users = []
    for obj in result:
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

# --------------
#   
@router.get("/usuarios/usuario/", tags=["usuarios"])
async def get_usuario_by_document(document: Dict[str, Any]):
    """lista os usuários"""
    obj = mongo_client.find_one_document("usuarios", document)

    result = {
        "id": str(obj["_id"]),
        "nome": obj["nome"],
        "sobrenome": obj["sobrenome"],
        "criado_em": str(obj["criado_em"]),
        "atualizado_em": str(obj["atualizado_em"]),
        "deletado": obj["deletado"]
    }

    return JSONResponse(result, status_code=200)

# --------------
#   
@router.put("/usuarios/id/{id}", tags=["usuarios"])
async def put_usuario(id: str, document: Dict[str, Any]):
    """Atualiza todos os campos"""

    document.update({
        "atualizado_em": datetime.now(),
        })

    result = mongo_client.update_document("usuarios", {"_id": ObjectId(str(id))}, document)

    if 'Erro' in result:
        return JSONResponse(result, status_code=400)
    else:
        return JSONResponse(result, status_code=200)

# --------------
#   Usado para atualizar também o campo de "deletado"
@router.patch("/usuarios/id/{id}", tags=["usuarios"])
async def patch_usuario(id: str, document: Dict[str, Any]):
    """Atualiza um ou mais campos"""

    document.update({
        "atualizado_em": datetime.now(),
        })

    result = mongo_client.update_document("usuarios", {"_id": ObjectId(str(id))}, document)

    if 'Erro' in result:
        return JSONResponse(result, status_code=400)
    else:
        return JSONResponse(result, status_code=200)
    
# --------------
#   Usado para atualizar também o campo de "deletado"
@router.delete("/usuarios/id/{id}", tags=["smart"])
async def delete_usuario(id: str):
    """Deleta um documento específico"""

    result = mongo_client.delete_document("usuarios", {"_id": ObjectId(str(id))})

    if 'Erro' in result:
        return JSONResponse(result, status_code=400)
    else:
        return JSONResponse(result, status_code=200)