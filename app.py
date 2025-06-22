from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import send_file
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
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

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Modelo de usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# Importa o CRUD de fornecedores
from sap_organizador.crud_fornecedores import cadastrar_fornecedor, listar_fornecedores

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

# Rota do painel com CRUD
@app.route("/painel", methods=["GET", "POST"])
@app.route("/painel", methods=["GET", "POST"])
def painel():
    if "usuario" not in session:
        return redirect(url_for("login"))

    obra_atual = "Vitale Santo André"
    cor_obra = "#6A1B9A" if obra_atual == "Vitale Santo André" else "#004d40"

    if request.method == "POST":
        nome = request.form["nome"]
        cnpj = request.form["cnpj"]
        cadastrar_fornecedor(nome, cnpj)

    fornecedores = listar_fornecedores()
    return render_template(
        "painel.html",
        usuario=session["usuario"],
        fornecedores=fornecedores,
        cor_obra=cor_obra,
        obra=obra_atual
    )
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

# Função para gerar relatório PDF com logo
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile

@app.route("/relatorio_fornecedores")
def relatorio_fornecedores():
    if "usuario" not in session:
        return redirect(url_for("login"))

    fornecedores = listar_fornecedores()

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp.name, pagesize=A4)
    largura, altura = A4

    caminho_logo = os.path.join(app.root_path, 'static', 'logo_obra.jpg')
    c.drawImage(caminho_logo, x=40, y=altura - 80, width=120, height=50, mask='auto')

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(largura / 2, altura - 50, "Relatório de Fornecedores")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, altura - 110, "ID")
    c.drawString(100, altura - 110, "Nome")
    c.drawString(350, altura - 110, "CNPJ")

    y = altura - 130
    c.setFont("Helvetica", 10)
    for f in fornecedores:
        c.drawString(50, y, str(f[0]))
        c.drawString(100, y, f[1])
        c.drawString(350, y, f[2] or "-")
        y -= 20
        if y < 50:
            c.showPage()
            y = altura - 50

    c.showPage()
    c.save()
    temp.close()

    from flask import send_file
    return send_file(temp.name, as_attachment=True, download_name="relatorio_fornecedores.pdf")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
