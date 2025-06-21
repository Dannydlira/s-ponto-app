from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chave_padrao")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

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
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
@app.route("/painel")
def painel():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("painel.html", usuario=session["usuario"])

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
