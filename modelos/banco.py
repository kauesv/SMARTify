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

    def insert_document(self, collection_name: str, document: dict):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(document)
            return {'id': result.inserted_id}
        except PyMongoError as e:
            print(f"Erro ao inserir documento: {e}")
            return {'Erro': str(e)}