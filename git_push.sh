#!/data/data/com.termux/files/usr/bin/bash
cd ~/downloads/s-ponto-termux || {
  echo "❌ Diretório do projeto não encontrado!"
  exit 1
}

# Verifica se é um repositório Git
if [ ! -d ".git" ]; then
  echo "❌ Este diretório não é um repositório Git."
  echo "Rode 'git init' e configure o repositório remoto com:"
  echo "  git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git"
  exit 1
fi

echo "🔁 Atualizando repositório Git..."

git add .

# Verifica se há algo para commitar
if git diff --cached --quiet; then
  echo "⚠️ Nenhuma alteração detectada para commit."
  exit 0
fi

echo "Digite a mensagem do commit:"
read mensagem

git commit -m "$mensagem"
git push

echo "✅ Código enviado para o GitHub com sucesso!"

