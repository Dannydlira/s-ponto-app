#!/data/data/com.termux/files/usr/bin/bash

# Entrar na pasta do projeto
cd ~/downloads/s-ponto-termux/sap_organizador

# Ativar ambiente virtual
source ../venv/bin/activate

# Exportar display para VNC
export DISPLAY=:1

# Rodar o programa Python
python main.py

# Após fechar o programa, sair da pasta (voltar para home)
cd ~/downloads/s-ponto-termux

echo "Programa finalizado e voltou para home."
