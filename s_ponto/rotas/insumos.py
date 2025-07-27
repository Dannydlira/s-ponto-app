# s_ponto/rotas/insumos.py

# --- Importações de Terceiros ---
from flask import Blueprint, render_template, request, redirect, url_for, flash

# --- Importações do Projeto ---
from ..modelos import db, Insumo, Fornecedor
from ..decorators import login_required

# --- Criação do Blueprint ---
# Criamos um "grupo de rotas" SÓ para insumos
insumos_bp = Blueprint('insumos', __name__, url_prefix='/insumos')

# --- Rotas ---

@insumos_bp.route('/')
@login_required
def listar():
    insumos = Insumo.query.all()
    # Garanta que seu template esteja em: s_ponto/templates/insumos/listar.html
    return render_template('insumos/listar.html', insumos=insumos)

@insumos_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    fornecedores = Fornecedor.query.all()
    if request.method == 'POST':
        i = Insumo(
            nome=request.form['nome'],
            tipo=request.form.get('tipo'),
            fornecedor_id=request.form.get('fornecedor_id')
        )
        db.session.add(i)
        db.session.commit()
        flash('Insumo cadastrado!')
        return redirect(url_for('insumos.listar'))
    # Garanta que seu template esteja em: s_ponto/templates/insumos/formulario.html
    return render_template('insumos/formulario.html', fornecedores=fornecedores)

@insumos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    insumo = Insumo.query.get_or_404(id)
    fornecedores = Fornecedor.query.all()
    if request.method == 'POST':
        insumo.nome = request.form['nome']
        insumo.tipo = request.form.get('tipo')
        insumo.fornecedor_id = request.form.get('fornecedor_id')
        db.session.commit()
        flash('Insumo atualizado!')
        return redirect(url_for('insumos.listar'))
    return render_template('insumos/formulario.html', insumo=insumo, fornecedores=fornecedores)

@insumos_bp.route('/excluir/<int:id>', methods=['POST'])
@login_required
def excluir(id):
    insumo = Insumo.query.get_or_404(id)
    db.session.delete(insumo)
    db.session.commit()
    flash('Insumo excluído!')
    return redirect(url_for('insumos.listar'))