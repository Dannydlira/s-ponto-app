# run.py - O PONTO DE PARTIDA DO SEU PROJETO

# Importa a função de fábrica de dentro do seu pacote 's_ponto'
from s_ponto import create_app
# Importa o 'db' para podermos criar as tabelas
from s_ponto.modelos import db

# Chama a fábrica para construir a instância do app
app = create_app()

# Este bloco só roda quando você executa 'python run.py' diretamente
if __name__ == '__main__':
    # Usamos o contexto do app para garantir que as tabelas existam
    with app.app_context():
        db.create_all()
    
    # Inicia o servidor de desenvolvimento
    app.run(debug=True, host="0.0.0.0", port=5000)