from s_ponto import app, db

print("📦 Criando tabelas no banco de dados...")

with app.app_context():
    db.create_all()

print("✅ Tabelas criadas com sucesso!")
