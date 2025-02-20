# Imagem base Python
FROM python:3.12-slim

# Atualizar o sistema e instalar dependências essenciais
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    g++ \
    make \
    wget \
    curl \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar as bibliotecas Python necessárias
RUN pip install --no-cache-dir spacy

# Instalar o modelo de linguagem do Spacy para o português
RUN python -m spacy download pt_core_news_lg

# Definir diretório de trabalho
WORKDIR /app
