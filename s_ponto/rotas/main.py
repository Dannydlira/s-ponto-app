# s_ponto/rotas/main.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
# Importa o decorator do seu novo arquivo
from ..decorators import login_required
# Importa os modelos necessários
from ..modelos import db, Usuario

# Criamos o Blueprint para as rotas principais
main_bp = Blueprint('main', __name__)

# ROTA LOGIN
@main_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = Usuario.query.filter_by(username=request.form["username"]).first()
        if usuario and usuario.senha == request.form["senha"]:
            session["usuario"] = usuario.username
            flash("Login realizado com sucesso!", "success")
            # Ajuste no url_for para usar o nome do blueprint
            return redirect(url_for("main.painel"))
        else:
            flash("Usuário ou senha inválidos.", "danger")
    return render_template("login.html")

# ROTA LOGOUT
@main_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Você saiu do sistema.", "info")
    return redirect(url_for("main.login"))

# ROTA PAINEL (home após login)
@main_bp.route("/painel")
@login_required
def painel():
    obra_atual = "Vitale Santo André"
    cor_obra = "#6A1B9A" if obra_atual == "Vitale Santo André" else "#004d40"
    return render_template("painel.html", usuario=session["usuario"], obra=obra_atual, cor_obra=cor_obra)