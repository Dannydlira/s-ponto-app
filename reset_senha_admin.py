from sap_organizador.app import app, db
from sap_organizador.modelos import Usuario

with app.app_context():
    usuario = Usuario.query.filter_by(username="admin").first()
    if not usuario:
        print("Usuário admin não encontrado.")
    else:
        nova_senha = input("Digite a nova senha para o admin (sem hash): ")
        usuario.senha = nova_senha
        db.session.commit()
        print("Senha atualizada com sucesso.")

