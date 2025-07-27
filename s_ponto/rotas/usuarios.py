# s_ponto/rotas/usuarios.py

# --- Importações de Terceiros ---
from flask import Blueprint, render_template, request, redirect, url_for, flash

# --- Importações do Projeto ---
from ..modelos import db, Usuario
from ..decorators import login_required

# --- Criação do Blueprint ---
usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# --- Rotas ---

@usuarios_bp.route("/")
@login_required
def listar():
    usuarios = Usuario.query.all()
    return render_template("usuarios.html", usuarios=usuarios)

@usuarios_bp.route("/novo", methods=["GET", "POST"])
@login_required
def novo():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]
        
        # Verificação se o usuário já existe (boa prática)
        existente = Usuario.query.filter_by(username=username).first()
        if existente:
            flash("Este nome de usuário já está em uso.", "danger")
            return render_template("form_usuario.html")

        u = Usuario(username=username, senha=senha)
        db.session.add(u)
        db.session.commit()
        flash("Usuário criado com sucesso.", "success")
        return redirect(url_for("usuarios.listar"))
    return render_template("form_usuario.html")

@usuarios_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    u = Usuario.query.get_or_404(id)
    if request.method == "POST":
        u.username = request.form["username"]
        u.senha = request.form["senha"]
        db.session.commit()
        flash("Usuário atualizado.", "success")
        return redirect(url_for("usuarios.listar"))
    return render_template("form_usuario.html", usuario=u)

@usuarios_bp.route("/excluir/<int:id>", methods=["POST"])
@login_required
def excluir(id):
    u = Usuario.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    flash("Usuário excluído.", "info")
    return redirect(url_for("usuarios.listar"))