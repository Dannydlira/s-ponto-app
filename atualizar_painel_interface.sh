#!/data/data/com.termux/files/usr/bin/bash

echo "🔧 Atualizando a função painel() no app.py..."

cat > temp_painel.py <<EOF
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
EOF

# Substitui a função painel no app.py
sed -i '/@app.route(\"\/painel\"/,/@app.route/ {
    /@app.route/!d
}' app.py

# Insere a nova função
sed -i "/@app.route(\"\/painel\"/r temp_painel.py" app.py
rm temp_painel.py
echo "✅ Função painel atualizada com sucesso!"

echo "🎨 Atualizando templates/painel.html..."

cat > templates/painel.html <<'EOF'
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <title>Painel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: {{ cor_obra }};
            color: white;
            padding: 10px 20px;
        }
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .top-bar img {
            height: 50px;
            border-radius: 5px;
            margin-right: 15px;
        }
        .user-info {
            display: flex;
            align-items: center;
        }
        .logout {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        .logout:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <div class="top-bar">
            <div class="user-info">
                <img src="{{ url_for('static', filename='logo_obra.jpg') }}" alt="Logo" />
                <div>
                    <h2>{{ obra }}</h2>
                    <p>Bem-vindo(a), {{ usuario }}</p>
                </div>
            </div>
            <a href="{{ url_for('logout') }}" class="logout">Sair</a>
        </div>
    </header>

    <main style="padding: 20px;">
        <h3>Cadastrar Fornecedor</h3>
        <form method="POST" action="/painel">
            <input type="text" name="nome" placeholder="Nome do fornecedor" required />
            <input type="text" name="cnpj" placeholder="CNPJ" />
            <button type="submit">Cadastrar</button>
        </form>

        <h3>Lista de Fornecedores</h3>
        <ul>
            {% for fornecedor in fornecedores %}
                <li>{{ fornecedor[1] }} - {{ fornecedor[2] or "CNPJ não informado" }}</li>
            {% else %}
                <li>Não há fornecedores cadastrados.</li>
            {% endfor %}
        </ul>
    </main>
</body>
</html>
EOF

echo "✅ Interface HTML atualizada com sucesso!"
