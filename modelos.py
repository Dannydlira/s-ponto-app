from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fornecedor(db.Model):
    __tablename__ = "fornecedores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(18))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(255))

class Insumo(db.Model):
    __tablename__ = "insumos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(100))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
