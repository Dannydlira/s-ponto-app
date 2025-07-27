# s_ponto/rotas/importacao.py

# --- Importações da Biblioteca Padrão ---
import os

# --- Importações de Terceiros ---
import pandas as pd
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename

# --- Importações do Projeto ---
from ..decorators import login_required

# --- Criação do Blueprint ---
importacao_bp = Blueprint('importacao', __name__, url_prefix='/importar')

# --- Rota ---

@importacao_bp.route("/", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        arquivo = request.files.get("arquivo")

        # Validação robusta do arquivo
        if not arquivo or arquivo.filename == '':
            flash("Nenhum arquivo selecionado.", "warning")
            return redirect(url_for("importacao.upload"))

        filename = secure_filename(arquivo.filename)
        
        # Cria um caminho seguro para o upload na pasta 'instance'
        upload_folder = os.path.join(current_app.instance_path, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        caminho_arquivo = os.path.join(upload_folder, filename)
        
        arquivo.save(caminho_arquivo)

        try:
            # Leitura do arquivo com pandas
            if filename.endswith(".csv"):
                df = pd.read_csv(caminho_arquivo)
            elif filename.endswith(".xlsx"):
                df = pd.read_excel(caminho_arquivo)
            else:
                flash("Formato de arquivo não suportado. Use .csv ou .xlsx.", "danger")
                return redirect(url_for("importacao.upload"))

            # Gera uma pré-visualização em HTML para o template
            preview = df.head().to_html(classes="table table-striped", index=False)

            flash("Arquivo enviado com sucesso! Pré-visualização abaixo.", "success")
            return render_template("importar.html", preview=preview)

        except Exception as e:
            flash(f"Erro ao processar o arquivo: {e}", "danger")
            return redirect(url_for("importacao.upload"))

    # Renderiza a página de upload inicial
    return render_template("importar.html")
