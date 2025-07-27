# importar_fornecedores.py - VERSÃO COMPLETA E ATUALIZADA

import pandas as pd
# Importa o app e o db para termos o contexto da aplicação e do banco
from app import app, db
# Importa o modelo Fornecedor do seu arquivo de modelos
from modelos import Fornecedor

# Nome do seu arquivo de planilha (garanta que está na mesma pasta)
NOME_ARQUIVO_EXCEL = 'fornecedores.xlsx'

def importar_dados():
    """
    Lê os dados de uma planilha Excel, separa o código do nome do fornecedor,
    e insere os dados na tabela de fornecedores no banco de dados.
    """
    print(f"Iniciando a importação do arquivo: {NOME_ARQUIVO_EXCEL}")

    # O 'with app.app_context()' é CRUCIAL.
    # Ele cria o ambiente necessário para que o script possa acessar o banco de dados
    # configurado no seu app Flask.
with app.app_context():
    try:
        # Lê a planilha usando pandas
        df = pd.read_excel(NOME_ARQUIVO_EXCEL)

        # LINHA DE LIMPEZA ESSENCIAL:
        # Converte todas as células vazias (lidas como NaN pelo pandas) para None,
        # que é o valor que o banco de dados entende como NULO.
        df = df.where(pd.notnull(df), None)

        # Itera sobre cada linha da planilha
        for index, row in df.iterrows():
            
            # --- VERIFICAÇÃO "À PROVA DE BALAS" ---
            # Pega o nome da planilha
            nome_da_planilha = row['Nome']
            
            # Pula a linha se o nome for NULO ou se for um texto que SÓ CONTÉM ESPAÇOS
            if pd.isna(nome_da_planilha) or not str(nome_da_planilha).strip():
                continue # Pula para a próxima iteração do loop
            # ------------------------------------

            # A partir daqui, o código continua como antes, mas usando a variável que já pegamos
            nome_completo = nome_da_planilha
            
            codigo_fornecedor = None
            nome_fornecedor = nome_completo

            if nome_completo and isinstance(nome_completo, str) and ' ' in nome_completo:
                partes = nome_completo.split(' ', 1)
                if partes[0].isdigit():
                    codigo_fornecedor = partes[0]
                    nome_fornecedor = partes[1].strip()

            # Cria um novo objeto Fornecedor com os dados já tratados
            novo_fornecedor = Fornecedor(
                codigo=codigo_fornecedor,
                nome=nome_fornecedor,
                cnpj=row['CNPJ'],
                telefone=row['Telefone'],
                email=row['Email'],
                endereco=row['Endereco']
            )
            db.session.add(novo_fornecedor)

        db.session.commit()
        print(f"\nSUCESSO! {len(df)} registros de fornecedores foram processados e importados.")

    except Exception as e:
        db.session.rollback()
        print(f"\nERRO! A importação falhou. Nenhuma alteração foi salva no banco.")
        print(f"Detalhe do erro: {e}")

# Executa a função de importação quando o script é rodado diretamente
if __name__ == '__main__':
    importar_dados()