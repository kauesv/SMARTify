FROM python:3.12

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o código do projeto para dentro do container
COPY . /app

# Instalando as dependências
RUN apt-get update && \
    pip install --no-cache-dir -r requirements.txt

# desabilita o buffering, para sair no terminal
ENV PYTHONUNBUFFERED=1

# Exponha a porta que a aplicação vai usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
