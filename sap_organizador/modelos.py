from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Criando o objeto db, que será usado no app.py

class Usuario(db.Model):
    __tablename__ = "usuario"  # Ajuste conforme nome real no banco
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

class Fornecedor(db.Model):
    __tablename__ = "fornecedores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(18))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    insumos = db.relationship('Insumo', backref='fornecedor', lazy=True)

class Insumo(db.Model):
    __tablename__ = "insumos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(100))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
