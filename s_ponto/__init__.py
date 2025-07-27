# s_ponto/__init__.py - A FÁBRICA DE APLICATIVOS (VERSÃO FINAL E COMPLETA)

import os
from flask import Flask
from dotenv import load_dotenv

# Importamos a instância 'db' do nosso arquivo de modelos.
from .modelos import db

def create_app():
    """
    Cria, configura e retorna uma instância do aplicativo Flask.
    Esta função é a "fábrica".
    """
    # Usamos instance_relative_config=True para que o Flask procure a pasta 'instance'
    app = Flask(__name__, instance_relative_config=True)
    load_dotenv()

    # --- 1. CONFIGURAÇÃO DO APP ---
    app.secret_key = os.getenv("SECRET_KEY", "uma-chave-secreta-muito-segura")
    
    db_url = os.environ.get("DATABASE_URL")
    if db_url and db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql+psycopg://", 1)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # --- 2. INICIALIZAÇÃO DAS EXTENSÕES ---
    # "Casa" o db com o app, tornando-o utilizável pelas rotas
    db.init_app(app)

    # --- 3. REGISTRO DOS BLUEPRINTS (ROTAS) ---
    # As importações e registros acontecem DENTRO da função para evitar erros
    with app.app_context():
        # Importamos todos os nossos grupos de rotas (garanta que os nomes dos arquivos batem)
        from .rotas import main
        from .rotas import fornecedores
        from .rotas import usuarios
        from .rotas import insumos
        from .rotas import relatorios
        from .rotas import importacao

        # Registramos cada grupo de rotas no aplicativo
        app.register_blueprint(main.main_bp)
        app.register_blueprint(fornecedores.fornecedores_bp)
        app.register_blueprint(usuarios.usuarios_bp)
        app.register_blueprint(insumos.insumos_bp)
        app.register_blueprint(relatorios.relatorios_bp)
        app.register_blueprint(importacao.importacao_bp)

    # --- 4. RETORNA O APP PRONTO ---
    return app
