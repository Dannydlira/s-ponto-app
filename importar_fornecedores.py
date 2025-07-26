import pandas as pd
# Importante: Importe o 'app', o 'db' e o seu modelo 'Fornecedor' do seu arquivo principal
from app import app, db, Fornecedor 

# Nome do seu arquivo de planilha
NOME_ARQUIVO_EXCEL = 'fornecedores.xlsx'

def importar_dados():
    print(f"Iniciando a importação do arquivo: {NOME_ARQUIVO_EXCEL}")
    
    # O 'with app.app_context()' é CRUCIAL. 
    # Ele cria o ambiente necessário para que o script possa acessar o banco de dados
    # configurado no seu app Flask.
    with app.app_context():
        try:
            # Lê a planilha usando pandas
            df = pd.read_excel(NOME_ARQUIVO_EXCEL)
            
            # Itera sobre cada linha da planilha
            for index, row in df.iterrows():
                # Cria um novo objeto Fornecedor com os dados da linha
                novo_fornecedor = Fornecedor(
                    nome=row['Nome'],
                    cnpj=row['CNPJ'],
                    telefone=row['Telefone'],
                    email=row['Email'],
                    endereco=row['Endereço'],
                )
                # Adiciona o novo fornecedor à sessão do banco de dados
                db.session.add(novo_fornecedor)
            
            # Depois de adicionar todos, efetivamente salva tudo no banco de uma vez
            db.session.commit()
            print(f"Sucesso! {len(df)} fornecedores importados.")

        except Exception as e:
            # Em caso de erro, desfaz qualquer alteração
            db.session.rollback()
            print(f"Ocorreu um erro durante a importação: {e}")

# Executa a função de importação quando o script é rodado
if __name__ == '__main__':
    importar_dados()
