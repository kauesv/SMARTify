Em desenvolvimento, aguarde...


## Passo a passo para rodar o projeto
### 1. Instalar Dependências
- Baixe e instale o MongoDB e o NoSQLBooster no seu computador a partir de seus sites oficiais.

### 2. Clonar o Repositório
- Clone o código em uma pasta local:
    ```
    git clone https://github.com/kauesv/SMARTify.git
    ```

### 3. Criar Ambiente Virtual
- Crie um ambiente virtual (Windows):
    ```
    py -m venv venv
    ```

### 4. Ativar Ambiente Virtual
- Ative o ambiente virtual (Windows):
    ```
    env\Scripts\Activate
    ```

### 5. Instalar Dependências do Projeto
- Instale o FastAPI:
    ```
    pip install fastapi
    ```
- Instale o Uvicorn:
    ```
    pip install uvicorn
    ```
- Instale o Pymongo:
    ```
    pip install pymongo
    ```

### 6. Iniciar o Servidor
- Suba o servidor com Uvicorn:
    ```
    uvicorn main:app --reload
    ```

### 7. Configurar MongoDB
- Configure o MongoDB:
    - Acesse o NoSQLBooster.
    - Vá até a pasta documentacoes/mongodb, copie os scripts de criação das coleções de usuários e smart, e execute-os no NoSQLBooster.

### 8. Importar Coleções para o Postman
- Use o arquivo de documentação da API:
    - Encontre o arquivo na pasta documentacoes/api.
    - Importe-o no Postman para testar as rotas da API.
