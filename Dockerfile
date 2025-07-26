# Usa a imagem oficial do Python 3.12 slim
FROM python:3.12-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do seu projeto para dentro do container
COPY . /app

# Atualiza o sistema e instala dependências necessárias para compilação de pacotes Python com C extensions
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    git \
    curl \
    && apt-get clean

# Instala pandas e outras dependências do requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Comando padrão para rodar sua aplicação (ajuste conforme necessário)
CMD ["python", "app.py"]
