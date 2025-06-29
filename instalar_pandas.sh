#!/data/data/com.termux/files/usr/bin/bash

echo "🔄 Atualizando Termux..."
pkg update && pkg upgrade -y

echo "📦 Instalando dependências..."
pkg install -y clang python fftw libxml2 libxslt libjpeg-turbo freetype zlib openssl libffi

echo "🐍 Atualizando pip e ferramentas..."
pip install --upgrade pip setuptools wheel

echo "📊 Instalando numpy, pandas e openpyxl..."
pip install numpy
pip install pandas openpyxl

echo "✅ Verificando..."
python -c "import pandas, openpyxl; print('✅ pandas e openpyxl funcionando perfeitamente!')"
