from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
class Fornecedor(db.Model):
    __tablename__ = "fornecedores"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=True) 
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=True) # Permitindo CNPJ nulo
    telefone = db.Column(db.String(20), nullable=True)         # Permitindo telefone nulo
    email = db.Column(db.String(100), nullable=True)
    endereco = db.Column(db.String(255), nullable=True)

class Insumo(db.Model):
    __tablename__ = "insumos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(100))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
