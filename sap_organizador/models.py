from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cnpj = db.Column(db.String(50))

    insumos = db.relationship('Insumo', backref='fornecedor', lazy=True)

class Insumo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))
