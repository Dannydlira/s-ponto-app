# s_ponto/rotas/relatorios.py

# --- Importações da Biblioteca Padrão ---
import os
import io
import tempfile
from datetime import datetime

# --- Importações de Terceiros ---
from flask import Blueprint, send_file, make_response, current_app, flash, redirect, url_for
from weasyprint import HTML  # Mantenha comentado se não estiver usando a rota form_usuario

# Importações para a biblioteca ReportLab (PDF)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# --- Importações do Projeto ---
from ..modelos import db, Fornecedor, Insumo, Usuario
from ..decorators import login_required

# --- Criação do Blueprint ---
relatorios_bp = Blueprint('relatorios', __name__, url_prefix='/relatorios')

# --- Rotas de Geração de Relatórios ---

@relatorios_bp.route("/fornecedores")
@login_required
def fornecedores():
    fornecedores = Fornecedor.query.all()
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp.name, pagesize=A4)
    largura, altura = A4

    caminho_logo = os.path.join(current_app.root_path, 'static', 'logo_obra.jpg')
    try:
        c.drawImage(caminho_logo, x=40, y=altura - 80, width=120, height=50, mask='auto')
    except Exception as e:
        print(f"Aviso: Não foi possível carregar o logo no relatório de fornecedores. Erro: {e}")

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


@relatorios_bp.route("/insumos")
@login_required
def insumos():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4

    caminho_logo = os.path.join(current_app.root_path, "static", "logo_obra.jpg")
    try:
        logo = ImageReader(caminho_logo)
        pdf.drawImage(logo, 40, altura - 100, width=120, height=50)
    except Exception as e:
        print(f"Aviso: Não foi possível carregar o logo no relatório de insumos. Erro: {e}")

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

# A rota abaixo usa uma biblioteca diferente (WeasyPrint).
# Se você não a tiver instalada, pode dar erro.
# Para instalar: pip install WeasyPrint
@relatorios_bp.route("/form_usuario")
@login_required
def form_usuario():
    # Garanta que a importação do WeasyPrint está descomentada no topo do arquivo
    # from weasyprint import HTML
    
    # Seu código original para gerar o HTML
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
            .input-box { margin-bottom: 10px; }
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
    
    try:
        # Tenta importar o WeasyPrint aqui para evitar erro na inicialização do app
        from weasyprint import HTML
        
        # Gera o PDF a partir do HTML
        pdf = HTML(string=html_content).write_pdf()
        
        # Cria a resposta para o navegador
        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "inline; filename=formulario_usuario.pdf"
        return response

    except ImportError:
        # Se o WeasyPrint não estiver instalado, mostra uma mensagem de erro amigável
        flash("A biblioteca para gerar este PDF (WeasyPrint) não está instalada.", "danger")
        return redirect(url_for('main.painel')) # Redireciona de volta para o painel
    except Exception as e:
        # Pega outros possíveis erros na geração do PDF
        flash(f"Ocorreu um erro ao gerar o PDF: {e}", "danger")
        return redirect(url_for('main.painel'))