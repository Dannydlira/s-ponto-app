# s_ponto/modelos.py - VERSÃO FINAL E GARANTIDA

from flask_sqlalchemy import SQLAlchemy

# A instância do SQLAlchemy é criada aqui, uma única vez.
db = SQLAlchemy()

#
# --- DEFINIÇÃO DE TODOS OS SEUS MODELOS ---
#

class Usuario(db.Model):
    # Damos o nome exato da tabela no banco de dados
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

class Fornecedor(db.Model):
    # Damos o nome exato da tabela no banco de dados
    __tablename__ = 'fornecedores'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    endereco = db.Column(db.String(255), nullable=True)
    
    # Usando back_populates para um relacionamento explícito e robusto
    insumos = db.relationship('Insumo', back_populates='fornecedor')

class Insumo(db.Model):
    # Damos o nome exato da tabela no banco de dados
    __tablename__ = 'insumos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))
    
    # A chave estrangeira aponta para a TABELA.COLUNA correta
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'), nullable=True)
    
    # Relacionamento de volta para Fornecedor
    fornecedor = db.relationship('Fornecedor', back_populates='insumos')
