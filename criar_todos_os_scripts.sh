#!/data/data/com.termux/files/usr/bin/bash

PASTA=~/downloads/s-ponto-termux

echo "🔧 Criando scripts automatizados no diretório $PASTA..."

# Script: start_vnc.sh
cat > $PASTA/start_vnc.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
vncserver :1
echo
echo "✅ VNC iniciado no display :1 (porta 5901)"
echo "Use o VNC Viewer e conecte-se ao endereço: 127.0.0.1:5901"
EOF

# Script: stop_vnc.sh
cat > $PASTA/stop_vnc.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
vncserver -kill :1
echo "🛑 Servidor VNC encerrado."
EOF

# Script: run_sap.sh
cat > $PASTA/run_sap.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/downloads/s-ponto-termux/sap_organizador
source ../venv/bin/activate
export DISPLAY=:1
python main.py
cd ~/downloads/s-ponto-termux
echo "✅ Programa finalizado. Você voltou para a pasta do projeto."
EOF

# Script: git_push.sh
cat > $PASTA/git_push.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/downloads/s-ponto-termux
git add .
echo "Digite a mensagem do commit:"
read mensagem
git commit -m "$mensagem"
git push
echo "✅ Código enviado para o GitHub!"
EOF

# Permissões de execução
chmod +x $PASTA/*.sh

echo "✅ Todos os scripts foram criados com sucesso em $PASTA!"
echo "➡ Exemplos de uso:"
echo "$PASTA/start_vnc.sh"
echo "$PASTA/run_sap.sh"
echo "$PASTA/stop_vnc.sh"
echo "$PASTA/git_push.sh"
