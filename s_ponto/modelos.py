# s_ponto/modelos.py - VERSÃO FINAL CORRIGIDA

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    endereco = db.Column(db.String(255), nullable=True)
    
    # --- A CORREÇÃO ESTÁ AQUI ---
    # A linha de relacionamento foi COMPLETAMENTE REMOVIDA
    # para que o SQLAlchemy não tente mais ligar as tabelas.

class Insumo(db.Model):
    __tablename__ = 'insumos'
    id = db.Column(db.Integer, primary_key=True)
    material_codigo = db.Column(db.String(50), unique=True, nullable=False)
    texto_breve = db.Column(db.String(255), nullable=True)
    
    # As linhas de relacionamento e ForeignKey foram COMPLETAMENTE REMOVIDAS.