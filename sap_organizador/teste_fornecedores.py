from crud_fornecedores import cadastrar_fornecedor, listar_fornecedores

print("=== Cadastro de Fornecedores ===")
nome = input("Nome: ")
cnpj = input("CNPJ: ")

cadastrar_fornecedor(nome, cnpj)

print("\n📋 Lista de fornecedores:")
for f in listar_fornecedores():
    print(f)
