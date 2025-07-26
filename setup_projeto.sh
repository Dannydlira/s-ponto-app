#!/data/data/com.termux/files/usr/bin/bash

echo "Ativando ambiente virtual..."
source ~/downloads/s-ponto-termux/venv/bin/activate

echo "Copiando imagem da logo..."
~/downloads/s-ponto-termux/copiar_logo.sh

echo "Iniciando o servidor Flask..."
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
#!/data/data/com.termux/files/usr/bin/bash

echo "Ativando ambiente virtual..."
source ~/downloads/s-ponto-termux/venv/bin/activate

echo "Instalando dependências do requirements.txt..."
pip install -r ~/downloads/s-ponto-termux/requirements.txt

echo "Copiando imagem da logo..."
~/downloads/s-ponto-termux/copiar_logo.sh

echo "Iniciando o servidor Flask..."
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
