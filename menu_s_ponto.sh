#!/data/data/com.termux/files/usr/bin/bash

while true; do
  clear
  echo "🟣 MENU - SISTEMA S-PONTO (TERMUX)"
  echo "----------------------------------"
  echo "1 - Rodar o sistema principal (main.py)"
  echo "2 - Enviar código para o GitHub"
  echo "3 - Rodar sistema Web (app.py)"
  echo "4 - Atualizar Interface do Painel"
  echo "5 - Rodar Code Server"
  echo "0 - Sair"
  echo "----------------------------------"
  read -p "Escolha uma opção [0-5]: " opcao

  case $opcao in
    1)
      echo "⏳ Iniciando sistema principal (main.py)..."
      . venv/bin/activate
      python sap_organizador/main.py
      deactivate
      read -p "✔ Pressione Enter para voltar ao menu..."
      ;;
    2)
      ./git_push.sh
      read -p "✔ Pressione Enter para voltar ao menu..."
      ;;
    3)
      echo "⏳ Rodando sistema Flask (app.py)..."
      . venv/bin/activate
      python app.py
      deactivate
      read -p "✔ Pressione Enter para voltar ao menu..."
      ;;
    4)
      bash atualizar_painel_interface.sh
      read -p "✔ Pressione Enter para voltar ao menu..."
      ;;
    5)
      echo "⏳ Iniciando Code Server..."
      bash start-code-server.sh
    ;;

    0)
      echo "Saindo do sistema..."
      exit 0
      ;;
    *)
      echo "❌ Opção inválida! Tente novamente."
      read -p "Pressione Enter para voltar ao menu..."
      ;;
  esac
done

