FROM python:3.12

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o código do projeto para dentro do container
COPY . /app

# Instala as dependências
RUN apt-get update && \
    apt install python3-dotenv && \
    apt-get install -y --no-install-recommends \
        nano \
        tzdata && \
    # limpar o cache do apt.
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    #pip install python-dotenv && \
    pip install --no-cache-dir -r requirements.txt

# Configura o fuso horário
RUN ln -snf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Exponha a porta que a aplicação vai usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
