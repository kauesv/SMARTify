from datetime import datetime


def test_connect_to_mongodb(mongodb_client):
    """Testa conexão com o MongoDB"""
    assert mongodb_client.client is not None
    assert mongodb_client.db is not None

def test_insert_document(mongodb_client, collection_name_usuarios):
    """Testa inserção de documentos"""
    document = {
        "nome": "backend",
        "sobrenome": "teste",
        "criado_em": datetime.now(),
        "atualizado_em": datetime.now(),
        "deletado": False
    }

    result = mongodb_client.insert_document(collection_name_usuarios, document)
    assert "_id" in result

def test_update_document(mongodb_client, collection_name_usuarios):
    """Test updating a document"""
    document = {
        "nome": "backend Update",
        "sobrenome": "teste Update",
        "atualizado_em": datetime.now()
    }

    result = mongodb_client.update_document(collection_name_usuarios, {"nome": "backend"}, document)
    assert result == {"modified_count": 1}

def test_delete_document(mongodb_client, collection_name_usuarios):
    """Test deleting a document"""

    result = mongodb_client.delete_document(collection_name_usuarios, {"nome": "backend Update"})
    assert result == {"deleted_count": 1}