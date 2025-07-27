from s_ponto import app, db, Usuario

print("👤 Criando usuário admin...")

with app.app_context():
    # Verifica se já existe um usuário admin
    existente = Usuario.query.filter_by(username="admin").first()
    if existente:
        print("⚠️ Usuário 'admin' já existe.")
    else:
        admin = Usuario(username="admin", senha="admin123")  # você pode trocar a senha depois
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuário 'admin' criado com sucesso!")

