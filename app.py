from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# Chave secreta da sessão
app.secret_key = os.getenv("SECRET_KEY", "chave_padrao")

# Configuração do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa a extensão do SQLAlchemy
db = SQLAlchemy(app)

# Modelo de usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# Rota de login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = Usuario.query.filter_by(username=request.form["username"]).first()
        if usuario and usuario.senha == request.form["senha"]:
            session["usuario"] = usuario.username
            return redirect("/painel")
        else:
            return render_template("login.html", erro="Usuário ou senha inválidos")
    return render_template("login.html")

# Rota do painel
@app.route("/painel")
def painel():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("painel.html", usuario=session["usuario"])

# Rota de logout
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

# Inicia o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
