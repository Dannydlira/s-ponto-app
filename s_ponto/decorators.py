# s_ponto/decorators.py

from functools import wraps
from flask import session, flash, redirect, url_for

def login_required(f):
    """
    Decorator que verifica se um usuário está logado na sessão.
    Redireciona para a página de login caso contrário.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario" not in session:
            flash("Faça login para acessar esta página.", "warning")
            # Redireciona para a rota de login, que está no blueprint 'main'
            return redirect(url_for("main.login"))
        return f(*args, **kwargs)
    return decorated_function