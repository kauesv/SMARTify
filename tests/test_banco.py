import pytest
import os
from dotenv import load_dotenv
from pymongo.errors import PyMongoError
from pymongo import MongoClient
from modelos.banco import MongoDBClient


# --------------
#   configs
load_dotenv(dotenv_path='config/config.env')


def test_connect_to_mongodb():
    """Test connection to MongoDB"""
    uri = os.getenv('URI')
    database_name = os.getenv('TESTE_DATABASE_NAME')

    client = MongoDBClient(uri, database_name)
    assert client.client is not None
    assert client.db is not None

