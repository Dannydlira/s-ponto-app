#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux
git add .
echo "Digite a mensagem do commit:"
read mensagem
git commit -m "$mensagem"
git push
echo "✅ Código enviado para o GitHub!"
#!/data/data/com.termux/files/usr/bin/bash
