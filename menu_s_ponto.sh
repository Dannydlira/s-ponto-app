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
      bash ~/downloads/s-ponto-termux/start_vnc.sh
      read -p "Pressione ENTER para voltar ao menu..."
      ;;
    2)
      bash ~/downloads/s-ponto-termux/run_sap.sh
      read -p "Pressione ENTER para voltar ao menu..."
      ;;
    3)
      bash ~/downloads/s-ponto-termux/git_push.sh
      read -p "Pressione ENTER para voltar ao menu..."
      ;;
    4)
      bash ~/downloads/s-ponto-termux/stop_vnc.sh
      read -p "Pressione ENTER para voltar ao menu..."
      ;;
    5)
      echo "Saindo do menu. Até mais!"
      break
      ;;
    *)
      echo "❌ Opção inválida! Tente novamente."
      sleep 1
      ;;
  esac
done
