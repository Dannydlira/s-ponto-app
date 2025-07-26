import psycopg2
import os
from dotenv import load_dotenv
import re

load_dotenv()

def conectar():
    url = os.getenv("DATABASE_URL")
    # Quebra a URL do tipo: postgresql://usuario:senha@host:porta/banco
    pattern = r'postgresql://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)'
    match = re.match(pattern, url)

    if not match:
        raise Exception("DATABASE_URL inválida!")

    user, password, host, port, dbname = match.groups()

    return psycopg2.connect(
        host=host,
        database=dbname,
        user=user,
        password=password,
        port=port
    )
