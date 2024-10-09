from log.logger import get_logger
from config import Config
from database.banco import MongoDBClient
from datetime import datetime
from bson import ObjectId
#from pymongo import MongoClient


# --------------
#   log
logger = get_logger("UsuariosRepository")

class UsuariosRepository():

    def __init__(self):
        # self.client = MongoClient(Config.BANCO_URI)
        # self.db = self.client[Config.DATABASE_NAME]
        self.db = MongoDBClient(Config.BANCO_URI, Config.DATABASE_NAME)
        self.collection = self.db[Config.COLLECTION_USUARIOS]

    def get_collection(self):
        return self.collection

    def insert_usuario(self, document):
        """inseri um usuario em uma collection"""

        result = self.collection.insert_one(document)

        logger.info(f'Usuário criado, ID:{str(result['_id'])}')
        return result

    def get_usuarios(self):
        """Retorna todos os usuarios de uma collection"""
        result = self.collection.find({})

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
        return list_users

    def update_data(self, id_usuario, document):
        """Atualiza um usuario em uma collection"""

        document.update({
            "atualizado_em": datetime.now(),
            })

        result = self.collection.update_one({"_id": ObjectId(str(id_usuario))}, {"$set": document})
        logger.info(f'Usuário atualizado, ID:{str(id_usuario)}')
        return result

    def remove_usuarios(self, list_usuarios):
        """Remove todos os documentos relacionados a um ou mais usuarios de uma collection"""
        query = {
            '_id': {'$in': list_usuarios}
        }

        result = self.collection.delte_many(query)

        logger.info(f'{result['deleted_count']} documents deleted')
        return result