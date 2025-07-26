#!/data/data/com.termux/files/usr/bin/bash
cd ~/downloads/s-ponto-termux/sap_organizador
source ../venv/bin/activate
export DISPLAY=:1
python main.py
cd ~/downloads/s-ponto-termux
echo "✅ Programa finalizado. Você voltou para a pasta do projeto."
