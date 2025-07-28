# importar_insumos.py - VERSÃO SIMPLIFICADA

import pandas as pd
from s_ponto import create_app
from s_ponto.modelos import db, Insumo

# Nome do seu arquivo de planilha
NOME_ARQUIVO_EXCEL = 'dados_sap.xlsx' # Use um nome novo para a planilha

def importar_insumos_simplificado():
    print(f"Iniciando a importação do arquivo: {NOME_ARQUIVO_EXCEL}")

    app = create_app()
    with app.app_context():
        try:
            df = pd.read_excel(NOME_ARQUIVO_EXCEL)
            
            # Limpeza dos dados
            df.columns = df.columns.str.strip()
            df = df.where(pd.notnull(df), None)

            insumos_importados = 0
            
            for index, row in df.iterrows():
                # Pega os dados das colunas da planilha
                codigo = str(row['Material']) if row['Material'] else None
                texto = row['Texto breve']

                if not codigo:
                    print(f"  - Linha {index+2} pulada: código do material está vazio.")
                    continue

                # Verifica se um insumo com este código já existe no banco
                insumo_existente = Insumo.query.filter_by(material_codigo=codigo).first()
                
                if insumo_existente:
                    # print(f"  - Insumo com código {codigo} já existe. Pulando.")
                    continue
                else:
                    # Se não existe, cria um novo
                    print(f"  -> Adicionando novo insumo: {codigo} - {texto}")
                    novo_insumo = Insumo(
                        material_codigo=codigo,
                        texto_breve=texto
                    )
                    db.session.add(novo_insumo)
                    insumos_importados += 1

            db.session.commit()
            print(f"\nSUCESSO! {insumos_importados} novos insumos foram importados.")

        except KeyError as e:
            db.session.rollback()
            print(f"\nERRO DE COLUNA! A importação falhou.")
            print(f"Verifique se a coluna '{e}' existe EXATAMENTE como está escrita no seu arquivo Excel.")
        except Exception as e:
            db.session.rollback()
            print(f"\nERRO! A importação falhou.")
            print(f"Detalhe do erro: {e}")

if __name__ == '__main__':
    importar_insumos_simplificado()