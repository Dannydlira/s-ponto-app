import os
from flask import Flask, render_template, request, redirect, url_for, session
from sap_organizador.modelos import db, Usuario
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'sap_organizador', 'templates'))
app.secret_key = os.getenv("SECRET_KEY", "chave_padrao")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("Banco usado:", app.config["SQLALCHEMY_DATABASE_URI"])

db.init_app(app)

# Importa o blueprint APÓS criar app e db
from sap_organizador.routes_insumos import insumos_bp
app.register_blueprint(insumos_bp, url_prefix='', name='insumos')

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

@app.route("/painel")
def painel():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template(
        "painel.html",
        usuario=session["usuario"],
        obra="Vitale Santo André",  # ou dinâmica depois
        cor_obra="#6A1B9A"  # roxo da identidade visual
    )

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

@app.route('/')
def home():
    return "Sistema S-Ponto funcionando!"

# ✅ BLOCO FINAL ÚNICO, COM `db.create_all()` E PORTA DEFINIDA
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
