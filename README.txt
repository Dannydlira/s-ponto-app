📦 Instruções para rodar no Termux:

1. Extraia este zip:
   unzip s-ponto-termux.zip
   cd s-ponto-termux

2. Instale dependências:
   pkg install python git
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate

3. Instale os pacotes do projeto:
   pip install -r requirements.txt

4. Configure o .env:
   cp .env.example .env
   nano .env  (adicione sua SECRET_KEY)

5. Rode o app:
   python app.py

Acesse pelo navegador: http://localhost:5000
Usuário de exemplo: (você pode criar um via banco sqlite diretamente)
