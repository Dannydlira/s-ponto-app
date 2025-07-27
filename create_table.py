from s_ponto import db

class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(18))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(255))

    insumos = db.relationship('Insumo', backref='fornecedor', lazy=True)

class Insumo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(100))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))
