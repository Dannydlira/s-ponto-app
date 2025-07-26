#!/data/data/com.termux/files/usr/bin/bash

echo "Criando pasta static no projeto (se não existir)..."
mkdir -p ~/downloads/s-ponto-termux/static

echo "Copiando logo_obra.jpg da pasta Download para static..."
cp /storage/emulated/0/Download/logo_obra.jpg ~/downloads/s-ponto-termux/static/

echo "Listando arquivos na pasta static:"
ls -l ~/downloads/s-ponto-termux/static

echo "Pronto! Agora a imagem está na pasta static."
