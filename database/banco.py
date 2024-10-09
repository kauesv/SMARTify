from pymongo import MongoClient
from pymongo.errors import PyMongoError

class MongoDBClient:
    def __init__(self, uri: str, database_name: str):
        self.client = None
        self.database_name = database_name
        self.connect(uri)

    def connect(self, uri: str):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[self.database_name]
            print("Conectado ao MongoDB.")
        except PyMongoError as e:
            print(f"Erro ao conectar ao MongoDB: {e}")

    # def insert_document(self, collection_name: str, document: dict):
    #     try:
    #         collection = self.db[collection_name]
    #         result = collection.insert_one(document)
    #         return {'_id': result.inserted_id}
    #     except PyMongoError as e:
    #         #print(f"Erro ao inserir documento: {e}")
    #         return {'Erro': str(e)}

    # def find_one_document(self, collection_name: str, query: dict):
    #     try:
    #         collection = self.db[collection_name]
    #         return collection.find_one(query)
    #     except PyMongoError as e:
    #         #print(f"Erro ao encontrar documento: {e}")
    #         return {'Erro': str(e)}

    # def find_document(self, collection_name: str, query: dict):
    #     try:
    #         collection = self.db[collection_name]
    #         return collection.find(query)
    #     except PyMongoError as e:
    #         #print(f"Erro ao encontrar documento: {e}")
    #         return {'Erro': str(e)}

    # def update_document(self, collection_name: str, query: dict, update: dict):
    #     try:
    #         collection = self.db[collection_name]
    #         result = collection.update_one(query, {"$set": update})
    #         return {'modified_count': result.modified_count}
    #     except PyMongoError as e:
    #         #print(f"Erro ao atualizar documento: {e}")
    #         return {'Erro': str(e)}

    # def delete_document(self, collection_name: str, query: dict):
    #     try:
    #         collection = self.db[collection_name]
    #         result = collection.delete_one(query)
    #         return {'deleted_count': result.deleted_count}
    #     except PyMongoError as e:
    #         #print(f"Erro ao remover documento: {e}")
    #         return {'Erro': str(e)}

    # def delete_documents(self, collection_name: str, query: dict):
    #     try:
    #         collection = self.db[collection_name]
    #         result = collection.delte_many(query)
    #         return {'deleted_count': result.deleted_count}
    #     except PyMongoError as e:
    #         #print(f"Erro ao remover documento: {e}")
    #         return {'Erro': str(e)}

    # def drop_database(self):
    #     try:
    #         self.client.drop_database(self.database_name)
    #         print("Excluindo o banco de dados")
    #     except PyMongoError as e:
    #         #print(f"Erro ao remover documento: {e}")
    #         return {'Erro': str(e)}

    # def drop_collection(self, collection_name: str):
    #     try:
    #         collection = self.db[collection_name]
    #         collection.drop()
    #         print("Excluindo a coleção do banco de dados")
    #     except PyMongoError as e:
    #         #print(f"Erro ao remover documento: {e}")
    #         return {'Erro': str(e)}