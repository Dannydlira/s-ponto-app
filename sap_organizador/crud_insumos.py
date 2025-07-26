# sap_organizador/crud_insumos.py
from .bd import conectar

def cadastrar_insumo(nome, tipo, fornecedor_id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO insumos (nome, tipo, fornecedor_id) VALUES (%s, %s, %s)", (nome, tipo, fornecedor_id))
    conn.commit()
    cur.close()
    conn.close()

def listar_insumos():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        SELECT insumos.id, insumos.nome, insumos.tipo, fornecedores.nome
        FROM insumos
        LEFT JOIN fornecedores ON insumos.fornecedor_id = fornecedores.id
    """)
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado
