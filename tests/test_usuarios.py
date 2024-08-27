from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

class TestUsuariosAPI:

    def test_post_usuario(self, test_document_usuarios):
        """"""
        response = client.post("/usuarios/", params=test_document_usuarios)

        assert response.status_code == 200
        assert "id" in response.json()

        # Deleta o que foi criado:
        client.delete(f"/usuarios/id/{response.json()['id']}")

    def test_delete_usuario(self, test_document_usuarios):
        """"""
        # Cria um usuario
        response_post = client.post("/usuarios/", params=test_document_usuarios)
        obj_id = str(response_post.json()["id"])

        response_del = client.delete(f"/usuarios/id/{obj_id}")
        assert response_del.status_code == 200
        assert response_del.json() == {"deleted_count": 1}

    def test_get_usuario_by_id(self, test_document_usuarios):
        """"""
        # Cria um usuario
        response_post = client.post("/usuarios/", params=test_document_usuarios)
        obj_id = str(response_post.json()["id"])

        # Obtem usando o ID
        response_get = client.get(f"/usuarios/id/{obj_id}")

        assert response_get.status_code == 200
        assert response_get.json()['id'] == obj_id

        # Deleta o que foi criado:
        client.delete(f"/usuarios/id/{obj_id}")

    def test_get_list_usuario(self,):
        """"""
        response = client.get("/usuarios/")
        assert response.status_code == 200

    # def test_get_usuario_by_document(self, test_document_usuarios):
    #     # Cria um usuario
    #     response_post = client.post("/usuarios/", params=test_document_usuarios)
    #     obj_id = str(response_post.json()["id"])

    #     # Obtem usando o nome e sobrenome
    #     response_get = client.get("/usuarios/usuario/", json=test_document_usuarios)
    #     print(response_get.json())
    #     assert response_get.status_code == 200

    #     # Deleta o que foi criado:
    #     client.delete(f"/usuarios/id/{obj_id}")

    def test_put_usuario(self, test_document_usuarios):
        # Cria um usuarios
        response_post = client.post("/usuarios/", params=test_document_usuarios)
        obj_id = str(response_post.json()["id"])

        response_put = client.put(f"/usuarios/id/{obj_id}", json={"nome": "BackendTest_novo",
                                                                  "sobrenome": "BackendTest_novo"})
        assert response_put.status_code == 200
        assert response_put.json() == {"modified_count": 1}

        # Deleta o que foi criado:
        client.delete(f"/usuarios/id/{obj_id}")

    def test_patch_usuario(self, test_document_usuarios):
        """"""
        # Cria um usuario
        response_post = client.post("/usuarios/", params=test_document_usuarios)
        obj_id = str(response_post.json()["id"])

        response_patch = client.patch(f"/usuarios/id/{obj_id}", json={
            "deletado": True
        })
        assert response_patch.status_code == 200
        assert response_patch.json() == {"modified_count": 1}

        # Deleta o que foi criado:
        client.delete(f"/usuarios/id/{obj_id}")