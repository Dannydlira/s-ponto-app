#!/data/data/com.termux/files/usr/bin/bash

while true; do
  clear
  echo "🟣 MENU - SISTEMA S-PONTO (TERMUX)"
  echo "----------------------------------"
  echo "1 - Iniciar VNC"
  echo "2 - Rodar o sistema (main.py)"
  echo "3 - Enviar código para o GitHub"
  echo "4 - Encerrar VNC"
  echo "5 - Sair"
  echo "----------------------------------"
  read -p "Escolha uma opção [1-5]: " opcao

  case $opcao in
    1)
      ./start_vnc.sh
      read -p "Pressione Enter para voltar ao menu..."
      ;;
    2)
      source venv/bin/activate
      export DISPLAY=:1
      python sap_organizador/main.py
      read -p "Pressione Enter para voltar ao menu..."
      ;;
    3)
      ./git_push.sh
      read -p "Pressione Enter para voltar ao menu..."
      ;;
    4)
      ./stop_vnc.sh
      read -p "Pressione Enter para voltar ao menu..."
      ;;
    5)
      echo "Saindo do sistema..."
      exit 0
      ;;
    *)
      echo "Opção inválida! Tente novamente."
      read -p "Pressione Enter para voltar ao menu..."
      ;;
  esac
done
