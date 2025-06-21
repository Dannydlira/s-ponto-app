import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # Carrega variáveis do arquivo .env

DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Usando DATABASE_URL: {DATABASE_URL}")

try:
    print("🔄 Testando conexão com o banco de dados...")
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Conexão realizada com sucesso!")
    conn.close()
except Exception as e:
    print("❌ Falha ao conectar ao banco de dados:")
    print(e)
