#!/bin/bash

echo "🔧 Iniciando configuração do projeto..."

# Criar .env se não existir
if [ ! -f .env ]; then
  echo "📄 Criando arquivo .env..."
  cat <<EOF > .env
DATABASE_URL=postgresql://usuario:senha@host:porta/nome_do_banco
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=uma-chave-secreta-aqui
EOF
  echo "✅ .env criado com sucesso!"
else
  echo "ℹ️ Arquivo .env já existe. Pulando..."
fi

# Criar pasta instance se não existir
if [ ! -d "instance" ]; then
  echo "📁 Criando diretório instance/"
  mkdir instance
fi

# Ativar venv
if [ -d "venv" ]; then
  echo "🐍 Ativando ambiente virtual..."
  source venv/bin/activate
else
  echo "⚠️ Ambiente virtual não encontrado. Crie com: python -m venv venv"
  exit 1
fi

# Instalar dependências
echo "📦 Instalando dependências do requirements.txt..."
pip install -r requirements.txt

echo "✅ Projeto configurado com sucesso!"

