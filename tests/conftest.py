import pytest
import os
from modelos.banco import MongoDBClient
from dotenv import load_dotenv


# --------------
#   env
load_dotenv(dotenv_path='config/config.env')

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
    return os.getenv('TEST_URI')

# --------------
#   Global variable
@pytest.fixture(scope='session')
def database_name():
    return os.getenv('TEST_DATABASE_NAME')

# --------------
#   Global variable
@pytest.fixture(scope='session')
def collection_name_usuarios():
    return os.getenv('TEST_DATABASE_COLLECTION_USUARIOS')

# --------------
#   Global variable
@pytest.fixture(scope='session')
def collection_name_smart():
    return os.getenv('TEST_DATABASE_COLLECTION_SMART')