# s_ponto/rotas/fornecedores.py

# --- Importações de Terceiros ---
from flask import Blueprint, render_template, request, redirect, url_for, flash

# --- Importações do Projeto ---
from ..modelos import db, Fornecedor
from ..decorators import login_required

# --- Criação do Blueprint ---
fornecedores_bp = Blueprint('fornecedores', __name__, url_prefix='/fornecedores')

# --- Rotas ---

@fornecedores_bp.route("/")
@login_required
def listar():
    fornecedores = Fornecedor.query.all()
    # CORREÇÃO AQUI: Apontando para o novo caminho do template
    return render_template("fornecedores/listar.html", fornecedores=fornecedores)

@fornecedores_bp.route("/novo", methods=["GET", "POST"])
@login_required
def novo():
    if request.method == "POST":
        f = Fornecedor(
            nome=request.form["nome"],
            cnpj=request.form.get("cnpj"),
            telefone=request.form.get("telefone"),
            email=request.form.get("email")
        )
        db.session.add(f)
        db.session.commit()
        flash("Fornecedor criado com sucesso.", "success")
        return redirect(url_for("fornecedores.listar"))
    # CORREÇÃO AQUI: Apontando para o novo caminho do template
    return render_template("fornecedores/formulario.html")

@fornecedores_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    f = Fornecedor.query.get_or_404(id)
    if request.method == "POST":
        f.nome = request.form["nome"]
        f.cnpj = request.form.get("cnpj")
        f.telefone = request.form.get("telefone")
        f.email = request.form.get("email")
        db.session.commit()
        flash("Fornecedor atualizado.", "success")
        return redirect(url_for("fornecedores.listar"))
    # CORREÇÃO AQUI: Apontando para o novo caminho do template
    return render_template("fornecedores/formulario.html", fornecedor=f)

@fornecedores_bp.route("/excluir/<int:id>", methods=["POST"])
@login_required
def excluir(id):
    f = Fornecedor.query.get_or_404(id)
    db.session.delete(f)
    db.session.commit()
    flash("Fornecedor excluído.", "info")
    return redirect(url_for("fornecedores.listar"))