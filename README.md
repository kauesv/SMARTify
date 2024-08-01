Em desenvolvimento, aguarde...


Passo a passo para rodar o projeto:
1º baixe o MongoDB e NoSQLBooster em seu computador

2º Clone o código em uma pasta
    $ git clone https://github.com/kauesv/SMARTify.git

3º Crie a env (Windows):
    $ py -m venv env

4º Inicie a env (Windows):
    $ env/Scripts/Activate

5º Instale o FastAPI:
    $ pip install fastapi

6º Instale o servidor:
    $ pip install uvicorn

7º Instale o pymongo:
    $ pip install pymongo

8º Suba o servidor:
    $ uvicorn main:app --reload

9º Vai em documentacoes/mongodb copie a criação das coleções dos usuarios e smart, e execute no NoSQLBooster

9º Por fim, use o arquivo que esta em documentacoes/api e importe no Postman.