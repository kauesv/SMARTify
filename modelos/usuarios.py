from modelos.banco import MongoDBClient
from datetime import datetime


class Usuarios:
    bank_collection = "usuarios"

    def __init__(self, nome, sobrenome, mongo_client: MongoDBClient):
        self._nome = nome
        self._sobrenome = sobrenome
        self._mongo_client = mongo_client

    def __str__(self):
        return self._nome

    def save_to_db(self):
        """
        Salva o usuário na coleção 'usuarios' do banco de dados.
        """
        user_data = {
            "nome": self._nome,
            "sobrenome": self._sobrenome,
            "criado_em": datetime.now(),
            "atualizado_em": datetime.now(),
            "deletado": False
        }

        return self._mongo_client.insert_document(Usuarios.bank_collection, user_data)