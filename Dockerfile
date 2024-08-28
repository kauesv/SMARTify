# Usando uma imagem base do Python
FROM python:3.12-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos de requisitos para dentro do container
COPY requirements.txt .

# Instalando as dependências
RUN apt-get update && \
    pip install --no-cache-dir -r requirements.txt

# Copiando o código do projeto para dentro do container
COPY . /app

# Exponha a porta que a aplicação vai usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
