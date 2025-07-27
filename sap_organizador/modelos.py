# modelos.py - VERSÃO CORRIGIDA

from flask_sqlalchemy import SQLAlchemy

# A instância do SQLAlchemy é criada aqui, mas ainda não está ligada a nenhum app.
db = SQLAlchemy()

# Suas classes de modelo continuam exatamente iguais
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    endereco = db.Column(db.String(255), nullable=True)
    insumos = db.relationship('Insumo', backref='fornecedor', lazy=True)

class Insumo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=True)
