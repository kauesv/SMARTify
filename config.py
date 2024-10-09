from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Dirotórios
    LOG_PATH=os.getenv('LOG_PATH')

    #Banco
    BANCO_URI=os.getenv('URI')
    DATABASE_NAME=os.getenv('DATABASE_NAME')

    #Collections
    COLLECTION_USUARIOS=os.getenv('COLLECTION_USUARIOS')

    # API
    URL_API=os.getenv('URL_API')

    #Testes
    TEST_URI=os.getenv('TEST_URI')
    TEST_DATABASE_NAME=os.getenv('TEST_DATABASE_NAME')
    TEST_DATABASE_COLLECTION_USUARIOS=os.getenv('TEST_DATABASE_COLLECTION_USUARIOS')
    TEST_DATABASE_COLLECTION_SMART=os.getenv('TEST_DATABASE_COLLECTION_SMART')