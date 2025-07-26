from flask import Blueprint, render_template, request, redirect, url_for, flash
from sap_organizador.modelos import db, Fornecedor, Insumo

insumos_bp = Blueprint('insumos', __name__)

# --- Fornecedores ---

@insumos_bp.route('/fornecedores')
def listar_fornecedores():
    fornecedores = Fornecedor.query.all()
    return render_template('fornecedores/listar.html', fornecedores=fornecedores)

@insumos_bp.route('/fornecedores/novo', methods=['GET', 'POST'])
def novo_fornecedor():
    if request.method == 'POST':
        f = Fornecedor(
            nome=request.form['nome'],
            cnpj=request.form['cnpj'],
            telefone=request.form['telefone'],
            email=request.form['email']
        )
        db.session.add(f)
        db.session.commit()
        flash('Fornecedor cadastrado com sucesso!')
        return redirect(url_for('insumos.listar_fornecedores'))
    return render_template('fornecedores/formulario.html')

@insumos_bp.route('/fornecedores/editar/<int:id>', methods=['GET', 'POST'])
def editar_fornecedor(id):
    fornecedor = Fornecedor.query.get_or_404(id)
    if request.method == 'POST':
        fornecedor.nome = request.form['nome']
        fornecedor.cnpj = request.form['cnpj']
        fornecedor.telefone = request.form['telefone']
        fornecedor.email = request.form['email']
        db.session.commit()
        flash('Fornecedor atualizado!')
        return redirect(url_for('insumos.listar_fornecedores'))
    return render_template('fornecedores/formulario.html', fornecedor=fornecedor)

@insumos_bp.route('/fornecedores/excluir/<int:id>')
def excluir_fornecedor(id):
    fornecedor = Fornecedor.query.get_or_404(id)
    db.session.delete(fornecedor)
    db.session.commit()
    flash('Fornecedor excluído!')
    return redirect(url_for('insumos.listar_fornecedores'))

# --- Insumos ---

@insumos_bp.route('/insumos')
def listar_insumos():
    insumos = Insumo.query.all()
    return render_template('insumos/listar.html', insumos=insumos)

@insumos_bp.route('/insumos/novo', methods=['GET', 'POST'])
def novo_insumo():
    fornecedores = Fornecedor.query.all()
    if request.method == 'POST':
        i = Insumo(
            nome=request.form['nome'],
            tipo=request.form['tipo'],
            fornecedor_id=request.form['fornecedor_id']
        )
        db.session.add(i)
        db.session.commit()
        flash('Insumo cadastrado!')
        return redirect(url_for('insumos.listar_insumos'))
    return render_template('insumos/formulario.html', fornecedores=fornecedores)

@insumos_bp.route('/insumos/editar/<int:id>', methods=['GET', 'POST'])
def editar_insumo(id):
    insumo = Insumo.query.get_or_404(id)
    fornecedores = Fornecedor.query.all()
    if request.method == 'POST':
        insumo.nome = request.form['nome']
        insumo.tipo = request.form['tipo']
        insumo.fornecedor_id = request.form['fornecedor_id']
        db.session.commit()
        flash('Insumo atualizado!')
        return redirect(url_for('insumos.listar_insumos'))
    return render_template('insumos/formulario.html', insumo=insumo, fornecedores=fornecedores)

@insumos_bp.route('/insumos/excluir/<int:id>')
def excluir_insumo(id):
    insumo = Insumo.query.get_or_404(id)
    db.session.delete(insumo)
    db.session.commit()
    flash('Insumo excluído!')
    return redirect(url_for('insumos.listar_insumos'))
