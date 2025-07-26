import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import csv

ARQUIVO_DADOS = "dados/dados_sap.json"

# Criar arquivo JSON se não existir
def inicializar_dados():
    if not os.path.exists("dados"):
        os.makedirs("dados")
    if not os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "w") as f:
            json.dump({"fornecedores": [], "insumos": []}, f)

def carregar_dados():
    with open(ARQUIVO_DADOS, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(dados, f, indent=4)

# Adicionar novo fornecedor ou insumo
def adicionar_item(tipo, nome, descricao):
    dados = carregar_dados()
    dados[tipo].append({"nome": nome, "descricao": descricao})
    salvar_dados(dados)

# Importar CSV
def importar_csv(tipo):
    caminho = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if caminho:
        with open(caminho, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            dados = carregar_dados()
            for linha in leitor:
                dados[tipo].append({
                    "nome": linha.get("nome", ""),
                    "descricao": linha.get("descricao", "")
                })
            salvar_dados(dados)
            messagebox.showinfo("Importação", f"{tipo.capitalize()} importados com sucesso!")

# Buscar itens
def buscar(tipo, termo, lista):
    dados = carregar_dados()
    lista.delete(0, tk.END)
    for item in dados[tipo]:
        if termo.lower() in item["nome"].lower():
            lista.insert(tk.END, f"{item['nome']} - {item['descricao']}")

# Interface
def criar_interface():
    root = tk.Tk()
    root.title("Organizador de Insumos e Fornecedores")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    for tipo in ["insumos", "fornecedores"]:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=tipo.capitalize())

        entrada_nome = ttk.Entry(frame, width=40)
        entrada_nome.pack(pady=5)
        entrada_nome.insert(0, f"Nome do {tipo[:-1]}")

        entrada_desc = ttk.Entry(frame, width=40)
        entrada_desc.pack(pady=5)
        entrada_desc.insert(0, f"Descrição")

        def salvar(tipo=tipo):
            adicionar_item(tipo, entrada_nome.get(), entrada_desc.get())
            entrada_nome.delete(0, tk.END)
            entrada_desc.delete(0, tk.END)
            atualizar_lista(tipo, lista_resultado)

        btn_adicionar = ttk.Button(frame, text="Adicionar", command=salvar)
        btn_adicionar.pack(pady=5)

        btn_importar = ttk.Button(frame, text="Importar CSV", command=lambda t=tipo: importar_csv(t))
        btn_importar.pack(pady=5)

        entrada_busca = ttk.Entry(frame, width=40)
        entrada_busca.pack(pady=5)
        entrada_busca.insert(0, "Buscar...")

        lista_resultado = tk.Listbox(frame, width=60, height=10)
        lista_resultado.pack(pady=5)

        btn_buscar = ttk.Button(frame, text="Buscar", command=lambda t=tipo: buscar(t, entrada_busca.get(), lista_resultado))
        btn_buscar.pack(pady=5)

        def atualizar_lista(tipo, lista):
            lista.delete(0, tk.END)
            for item in carregar_dados()[tipo]:
                lista.insert(tk.END, f"{item['nome']} - {item['descricao']}")

        atualizar_lista(tipo, lista_resultado)

    root.mainloop()

# Execução
inicializar_dados()
criar_interface()
