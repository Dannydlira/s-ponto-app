import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# Banco SQLite no arquivo local na pasta do projeto
DB_PATH = os.path.join(os.path.dirname(__file__), 'sap.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cnpj TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS insumos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    fornecedor_id INTEGER,
    preco REAL,
    FOREIGN KEY(fornecedor_id) REFERENCES fornecedores(id)
)
''')
conn.commit()

def adicionar_fornecedor(nome, cnpj):
    cursor.execute('INSERT INTO fornecedores (nome, cnpj) VALUES (?, ?)', (nome, cnpj))
    conn.commit()

def listar_fornecedores():
    cursor.execute('SELECT * FROM fornecedores')
    return cursor.fetchall()

def adicionar_insumo(descricao, fornecedor_id, preco):
    cursor.execute('INSERT INTO insumos (descricao, fornecedor_id, preco) VALUES (?, ?, ?)',
                   (descricao, fornecedor_id, preco))
    conn.commit()

def listar_insumos():
    cursor.execute('''
    SELECT i.id, i.descricao, f.nome, i.preco
    FROM insumos i LEFT JOIN fornecedores f ON i.fornecedor_id = f.id
    ''')
    return cursor.fetchall()

class App:
    def __init__(self, root):
        self.root = root
        root.title("Organizador SAP - S-Ponto")

        tabControl = ttk.Notebook(root)
        self.tab_fornecedores = ttk.Frame(tabControl)
        self.tab_insumos = ttk.Frame(tabControl)
        tabControl.add(self.tab_fornecedores, text='Fornecedores')
        tabControl.add(self.tab_insumos, text='Insumos')
        tabControl.pack(expand=1, fill='both')

        # Fornecedores tab
        tk.Label(self.tab_fornecedores, text="Nome:").grid(row=0, column=0, sticky='e')
        self.fornecedor_nome = tk.Entry(self.tab_fornecedores)
        self.fornecedor_nome.grid(row=0, column=1, pady=5)

        tk.Label(self.tab_fornecedores, text="CNPJ:").grid(row=1, column=0, sticky='e')
        self.fornecedor_cnpj = tk.Entry(self.tab_fornecedores)
        self.fornecedor_cnpj.grid(row=1, column=1, pady=5)

        tk.Button(self.tab_fornecedores, text="Adicionar", command=self.add_fornecedor).grid(row=2, column=0, columnspan=2, pady=5)

        self.fornecedores_listbox = tk.Listbox(self.tab_fornecedores, width=50)
        self.fornecedores_listbox.grid(row=3, column=0, columnspan=2, pady=5)

        self.atualizar_fornecedores()

        # Insumos tab
        tk.Label(self.tab_insumos, text="Descrição:").grid(row=0, column=0, sticky='e')
        self.insumo_desc = tk.Entry(self.tab_insumos)
        self.insumo_desc.grid(row=0, column=1, pady=5)

        tk.Label(self.tab_insumos, text="Fornecedor:").grid(row=1, column=0, sticky='e')
        self.fornecedor_combobox = ttk.Combobox(self.tab_insumos, state='readonly')
        self.fornecedor_combobox.grid(row=1, column=1, pady=5)

        tk.Label(self.tab_insumos, text="Preço:").grid(row=2, column=0, sticky='e')
        self.insumo_preco = tk.Entry(self.tab_insumos)
        self.insumo_preco.grid(row=2, column=1, pady=5)

        tk.Button(self.tab_insumos, text="Adicionar", command=self.add_insumo).grid(row=3, column=0, columnspan=2, pady=5)

        self.insumos_listbox = tk.Listbox(self.tab_insumos, width=70)
        self.insumos_listbox.grid(row=4, column=0, columnspan=2, pady=5)

        self.atualizar_insumos()
        self.atualizar_fornecedores_combobox()

    def add_fornecedor(self):
        nome = self.fornecedor_nome.get()
        cnpj = self.fornecedor_cnpj.get()
        if not nome.strip():
            messagebox.showwarning("Aviso", "Nome é obrigatório")
            return
        adicionar_fornecedor(nome, cnpj)
        self.fornecedor_nome.delete(0, tk.END)
        self.fornecedor_cnpj.delete(0, tk.END)
        self.atualizar_fornecedores()
        self.atualizar_fornecedores_combobox()

    def atualizar_fornecedores(self):
        self.fornecedores_listbox.delete(0, tk.END)
        for f in listar_fornecedores():
            self.fornecedores_listbox.insert(tk.END, f"{f[1]} (CNPJ: {f[2] or 'N/A'})")

    def atualizar_fornecedores_combobox(self):
        fornecedores = listar_fornecedores()
        self.fornecedor_combobox['values'] = [f"{f[0]} - {f[1]}" for f in fornecedores]

    def add_insumo(self):
        desc = self.insumo_desc.get()
        preco = self.insumo_preco.get()
        fornecedor_val = self.fornecedor_combobox.get()
        if not desc.strip() or not fornecedor_val:
            messagebox.showwarning("Aviso", "Descrição e Fornecedor são obrigatórios")
            return
        try:
            preco_val = float(preco)
        except:
            preco_val = None
        fornecedor_id = int(fornecedor_val.split(" - ")[0])
        adicionar_insumo(desc, fornecedor_id, preco_val)
        self.insumo_desc.delete(0, tk.END)
        self.insumo_preco.delete(0, tk.END)
        self.atualizar_insumos()

    def atualizar_insumos(self):
        self.insumos_listbox.delete(0, tk.END)
        for i in listar_insumos():
            self.insumos_listbox.insert(tk.END, f"{i[1]} - {i[2] or 'Sem fornecedor'} - R$ {i[3] or '0.00'}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
