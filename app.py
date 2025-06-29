from flask import Flask, request, render_template, redirect, url_for, session, send_file, flash
from sap_organizador.modelos import db, Usuario, Fornecedor, Insumo
from dotenv import load_dotenv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import tempfile
from functools import wraps

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chave_padrao")

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Decorator para proteger rotas
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "usuario" not in session:
            flash("Faça login para acessar esta página.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# ROTA LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = Usuario.query.filter_by(username=request.form["username"]).first()
        if usuario and usuario.senha == request.form["senha"]:
            session["usuario"] = usuario.username
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("painel"))
        else:
            flash("Usuário ou senha inválidos.", "danger")
    return render_template("login.html")

# ROTA LOGOUT
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Você saiu do sistema.", "info")
    return redirect(url_for("login"))

# ROTA PAINEL (home após login)
@app.route("/painel")
@login_required
def painel():
    obra_atual = "Vitale Santo André"
    cor_obra = "#6A1B9A" if obra_atual == "Vitale Santo André" else "#004d40"
    return render_template("painel.html", usuario=session["usuario"], obra=obra_atual, cor_obra=cor_obra)

# -------------------------------
# CRUD FORNECEDORES
# -------------------------------
@app.route("/fornecedores")
@login_required
def listar_fornecedores():
    fornecedores = Fornecedor.query.all()
    return render_template("fornecedores.html", fornecedores=fornecedores)

@app.route("/fornecedores/novo", methods=["GET", "POST"])
@login_required
def novo_fornecedor():
    if request.method == "POST":
        nome = request.form["nome"]
        cnpj = request.form.get("cnpj")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        f = Fornecedor(nome=nome, cnpj=cnpj, telefone=telefone, email=email)
        db.session.add(f)
        db.session.commit()
        flash("Fornecedor criado com sucesso.", "success")
        return redirect(url_for("listar_fornecedores"))
    return render_template("form_fornecedor.html")

@app.route("/fornecedores/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_fornecedor(id):
    f = Fornecedor.query.get_or_404(id)
    if request.method == "POST":
        f.nome = request.form["nome"]
        f.cnpj = request.form.get("cnpj")
        f.telefone = request.form.get("telefone")
        f.email = request.form.get("email")
        db.session.commit()
        flash("Fornecedor atualizado.", "success")
        return redirect(url_for("listar_fornecedores"))
    return render_template("form_fornecedor.html", fornecedor=f)

@app.route("/fornecedores/excluir/<int:id>", methods=["POST"])
@login_required
def excluir_fornecedor(id):
    f = Fornecedor.query.get_or_404(id)
    db.session.delete(f)
    db.session.commit()
    flash("Fornecedor excluído.", "info")
    return redirect(url_for("listar_fornecedores"))

# -------------------------------
# CRUD INSUMOS
# -------------------------------
@app.route("/insumos")
@login_required
def listar_insumos():
    insumos = Insumo.query.all()
    fornecedores = Fornecedor.query.all()
    return render_template("insumos.html", insumos=insumos, fornecedores=fornecedores)

@app.route("/insumos/novo", methods=["GET", "POST"])
@login_required
def novo_insumo():
    fornecedores = Fornecedor.query.all()
    if request.method == "POST":
        nome = request.form["nome"]
        tipo = request.form.get("tipo")
        fornecedor_id = request.form.get("fornecedor_id")
        insumo = Insumo(nome=nome, tipo=tipo, fornecedor_id=fornecedor_id)
        db.session.add(insumo)
        db.session.commit()
        flash("Insumo criado com sucesso.", "success")
        return redirect(url_for("listar_insumos"))
    return render_template("form_insumo.html", fornecedores=fornecedores)

@app.route("/insumos/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_insumo(id):
    insumo = Insumo.query.get_or_404(id)
    fornecedores = Fornecedor.query.all()
    if request.method == "POST":
        insumo.nome = request.form["nome"]
        insumo.tipo = request.form.get("tipo")
        insumo.fornecedor_id = request.form.get("fornecedor_id")
        db.session.commit()
        flash("Insumo atualizado.", "success")
        return redirect(url_for("listar_insumos"))
    return render_template("form_insumo.html", insumo=insumo, fornecedores=fornecedores)

@app.route("/insumos/excluir/<int:id>", methods=["POST"])
@login_required
def excluir_insumo(id):
    insumo = Insumo.query.get_or_404(id)
    db.session.delete(insumo)
    db.session.commit()
    flash("Insumo excluído.", "info")
    return redirect(url_for("listar_insumos"))

# -------------------------------
# CRUD USUÁRIOS
# -------------------------------
@app.route("/usuarios")
@login_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios/novo", methods=["GET", "POST"])
@login_required
def novo_usuario():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]
        # Aqui você pode adicionar verificação se username já existe
        u = Usuario(username=username, senha=senha)
        db.session.add(u)
        db.session.commit()
        flash("Usuário criado com sucesso.", "success")
        return redirect(url_for("listar_usuarios"))
    return render_template("form_usuario.html")

@app.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_usuario(id):
    u = Usuario.query.get_or_404(id)
    if request.method == "POST":
        u.username = request.form["username"]
        u.senha = request.form["senha"]
        db.session.commit()
        flash("Usuário atualizado.", "success")
        return redirect(url_for("listar_usuarios"))
    return render_template("form_usuario.html", usuario=u)

@app.route("/usuarios/excluir/<int:id>", methods=["POST"])
@login_required
def excluir_usuario(id):
    u = Usuario.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    flash("Usuário excluído.", "info")
    return redirect(url_for("listar_usuarios"))

# -------------------------------
# Relatório PDF fornecedores (com logo)
# -------------------------------
@app.route("/relatorio_fornecedores")
@login_required
def relatorio_fornecedores():
    fornecedores = Fornecedor.query.all()
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
        c.drawString(50, y, str(f.id))
        c.drawString(100, y, f.nome)
        c.drawString(350, y, f.cnpj or "-")
        y -= 20
        if y < 50:
            c.showPage()
            y = altura - 50

    c.showPage()
    c.save()
    temp.close()

    return send_file(temp.name, as_attachment=True, download_name="relatorio_fornecedores.pdf")

from weasyprint import HTML
from datetime import datetime
from flask import make_response

# -------------------------------
# Relatório PDF Usuario (com logo)
# -------------------------------
@app.route("/relatorio_form_usuario")
@login_required
def relatorio_form_usuario():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Formulário de Usuário</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            form { max-width: 500px; margin: auto; background: #f9f9f9; padding: 20px; border-radius: 8px; }
            h2 { text-align: center; color: #333; }
            label { display: block; margin-top: 15px; font-weight: bold; }
            input {
                width: 100%; padding: 8px; margin-top: 5px;
                border: 1px solid #ccc; border-radius: 4px;
            }
            .input-box {
                margin-bottom: 10px;
            }
            .footer { text-align: center; margin-top: 30px; font-size: 12px; color: #888; }
        </style>
    </head>
    <body>
        <h2>Formulário de Usuário</h2>
        <form>
            <div class="input-box">
                <label>Usuário</label>
                <input type="text" placeholder="Digite o nome de usuário">
            </div>
            <div class="input-box">
                <label>Senha</label>
                <input type="password" placeholder="Digite a senha">
            </div>
        </form>
        <div class="footer">Gerado em: """ + datetime.now().strftime('%d/%m/%Y %H:%M') + """</div>
    </body>
    </html>
    """

    pdf = HTML(string=html_content).write_pdf()
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=formulario_usuario.pdf"
    return response

from datetime import datetime
from reportlab.lib.utils import ImageReader
import io

@app.route("/relatorio_insumos")
@login_required
def relatorio_insumos():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4

    # Caminho para o logo
    caminho_logo = os.path.join(app.root_path, "static", "logo_obra.jpg")

    try:
        logo = ImageReader(caminho_logo)
        pdf.drawImage(logo, 40, altura - 100, width=120, height=50)
    except Exception as e:
        print(f"Erro ao carregar logo: {e}")

    # Título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(largura / 2, altura - 60, "Relatório de Insumos")

    pdf.setFont("Helvetica", 11)
    y = altura - 130

    insumos = Insumo.query.all()
    for insumo in insumos:
        texto = f"ID: {insumo.id} | Nome: {insumo.nome} | Tipo: {insumo.tipo} | Fornecedor ID: {insumo.fornecedor_id}"
        pdf.drawString(40, y, texto)
        y -= 20
        if y < 70:
            pdf.showPage()
            y = altura - 50

    # Rodapé com data/hora
    data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawRightString(largura - 40, 30, f"Gerado em: {data_geracao}")

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="relatorio_insumos.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
