from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

class TestSmartAPI:
    def test_post_smart(self, test_document_sem_data):
        """"""
        response = client.post("/smart/", json=test_document_sem_data)

        assert response.status_code == 200
        assert "id" in response.json()

        # Deleta o que foi criado:
        client.delete(f"/smart/id/{response.json()['id']}")

    def test_delete_smart(self, test_document_sem_data):
        """"""
        # Cria um smart
        response_post = client.post("/smart/", json=test_document_sem_data)
        obj_id = str(response_post.json()["id"])

        response_del = client.delete(f"/smart/id/{obj_id}")
        assert response_del.status_code == 200
        assert response_del.json() == {"deleted_count": 1}

    def test_get_smart_by_id(self, test_document_sem_data):
        """"""
        # Cria um smart
        response_post = client.post("/smart/", json=test_document_sem_data)
        obj_id = str(response_post.json()["id"])

        # Obtem usando o ID
        response_get = client.get(f"/smart/id/{obj_id}")

        assert response_get.status_code == 200
        assert response_get.json()['id'] == obj_id
        assert response_get.json()['usuario_id'] == test_document_sem_data['usuario_id']

        # Deleta o que foi criado:
        client.delete(f"/smart/id/{obj_id}")

    def test_get_list_smart(self):
        """"""
        response = client.get("/smart/")
        
        assert response.status_code == 200

    def test_put_smart(self, test_document_sem_data):
        """"""
        # Cria um smart
        response_post = client.post("/smart/", json=test_document_sem_data)
        obj_id = str(response_post.json()["id"])

        response_put = client.put(f"/smart/id/{obj_id}", json={
            "especifica": "Novo valor",
            "mensuravel": "Novo valor",
            "atingivel": "Novo valor",
            "relevante": "Novo valor",
            "temporizavel": "Novo valor",
            "status": "Iniciada"
        })
        assert response_put.status_code == 200
        assert response_put.json() == {"modified_count": 1}

        # Deleta o que foi criado:
        client.delete(f"/smart/id/{obj_id}")

    def test_patch_smart(self, test_document_sem_data):
        """"""
        # Cria um smart
        response_post = client.post("/smart/", json=test_document_sem_data)
        obj_id = str(response_post.json()["id"])

        response_put = client.patch(f"/smart/id/{obj_id}", json={
            "deletado": True,
            "status": "Concluída"
        })
        assert response_put.status_code == 200
        assert response_put.json() == {"modified_count": 1}

        # Deleta o que foi criado:
        client.delete(f"/smart/id/{obj_id}")