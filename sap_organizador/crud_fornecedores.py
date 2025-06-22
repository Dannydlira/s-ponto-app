from .bd import conectar

def cadastrar_fornecedor(nome, cnpj):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO fornecedores (nome, cnpj) VALUES (%s, %s)", (nome, cnpj))
    conn.commit()
    cur.close()
    conn.close()

def listar_fornecedores():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fornecedores ORDER BY id")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado
