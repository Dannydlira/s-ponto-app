#!/data/data/com.termux/files/usr/bin/bash

echo "🛠️ Corrigindo repositório do Termux..."

# Corrigir o sources.list com o repositório oficial
cat <<EOF > $PREFIX/etc/apt/sources.list
deb https://packages.termux.dev/apt/termux-main stable main
EOF

echo "🔄 Atualizando pacotes..."
apt update && apt upgrade -y

echo "🧹 Limpando pacotes antigos..."
apt autoremove --purge -y

echo "📦 Instalando cmake, jsoncpp, libuv e rhash..."
pkg install -y cmake jsoncpp libuv rhash

echo "✅ Verificando instalação do cmake..."
cmake --version

echo "🎉 Finalizado! Ambiente pronto para uso."
