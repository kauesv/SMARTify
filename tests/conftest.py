import pytest
import os
from database.banco import MongoDBClient
from bson import ObjectId
from datetime import datetime
from config import Config


# --------------
#   Session, é chamada apenas uma vez. E o Yield deixa o client disponivel para no teste
@pytest.fixture(scope='session')
def mongodb_client(uri, database_name):
    """Fixture to set up MongoDB client."""
    client = MongoDBClient(uri, database_name)

    yield client

# --------------
#   Global variable
@pytest.fixture(scope='session')
def uri():
    return Config.TEST_URI

# --------------
#   Global variable
@pytest.fixture(scope='session')
def database_name():
    return Config.TEST_DATABASE_NAME

# --------------
#   Global variable
@pytest.fixture(scope='session')
def collection_name_usuarios():
    return Config.TEST_DATABASE_COLLECTION_USUARIOS

# --------------
#   Global variable
@pytest.fixture(scope='session')
def collection_name_smart():
    return Config.TEST_DATABASE_COLLECTION_SMART

# --------------
#   Global variable
@pytest.fixture(scope='session')
def url_api():
    return Config.URL_API

# --------------
#   Global variable
@pytest.fixture(scope='session')
def test_document_sem_data():
    """Simulação de dados para os testes"""
    return {
        "usuario_id": "BackendTest",
        "especifica": "Exemplo específico",
        "mensuravel": "Exemplo mensurável",
        "atingivel": "Exemplo atingível",
        "relevante": "Exemplo relevante",
        "temporizavel": "Exemplo temporizável",
        "status": "Não Iniciada"
    }

# --------------
#   Global variable
@pytest.fixture(scope='session')
def test_document_com_data():
    """Simulação de dados para os testes"""
    return {
        "usuario_id": "BackendTest",
        "especifica": "Exemplo específico",
        "mensuravel": "Exemplo mensurável",
        "atingivel": "Exemplo atingível",
        "relevante": "Exemplo relevante",
        "temporizavel": "Exemplo temporizável",
        "status": "Não Iniciada",
        "criado_em": datetime.now(),
        "atualizado_em": datetime.now(),
        "deletado": False
    }

# --------------
#   Global variable
@pytest.fixture(scope='session')
def test_document_usuarios():
    """Simulação de dados para os testes"""
    return {
        "nome": "BackendTest",
        "sobrenome": "BackendTest"
    }

# --------------
#   Global variable
@pytest.fixture(scope='session')
def test_id():
    """ID para os testes"""
    test_id = str(ObjectId())

    return test_id