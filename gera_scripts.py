import os
from zipfile import ZipFile

# Diretório temporário para montar os arquivos
base_dir = "/mnt/data/s-ponto-termux-kit"
os.makedirs(base_dir, exist_ok=True)

# Scripts e conteúdo do README
arquivos = {
    "start_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver :1
echo
echo "✅ VNC iniciado no display :1 (porta 5901)"
echo "Use o VNC Viewer e conecte-se ao endereço: 127.0.0.1:5901"
""",

    "stop_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver -kill :1
echo "🛑 Servidor VNC encerrado."
""",

    "run_sap.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux/sap_organizador
source ../venv/bin/activate
export DISPLAY=:1
python main.py
cd ~/downloads/s-ponto-termux
echo "✅ Programa finalizado. Você voltou para a pasta do projeto."
""",

    "git_push.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux
git add .
echo "Digite a mensagem do commit:"
read mensagem
git commit -m "$mensagem"
git push
echo "✅ Código enviado para o GitHub!"
""",

    "README.md": """# 🟣 S-Ponto Termux Kit

Este pacote contém scripts para facilitar a execução e manutenção do sistema S-Ponto no Termux com interface gráfica via VNC.

## ✅ Scripts incluídos

- `start_vnc.sh`: Inicia o servidor VNC no display :1
- `stop_vnc.sh`: Encerra o servidor VNC
- `run_sap.sh`: Ativa o ambiente virtual e executa o sistema com Tkinter
- `git_push.sh`: Faz commit e envia o projeto para o GitHub
- `README.md`: Este manual de uso

## 🧭 Como usar

### 1. Inicie o VNC:
```bash
./start_vnc.sh
import os
from zipfile import ZipFile

# Diretório temporário para montar os arquivos
base_dir = "/mnt/data/s-ponto-termux-kit"
os.makedirs(base_dir, exist_ok=True)

# Scripts e conteúdo do README
arquivos = {
    "start_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver :1
echo
echo "✅ VNC iniciado no display :1 (porta 5901)"
echo "Use o VNC Viewer e conecte-se ao endereço: 127.0.0.1:5901"
""",

    "stop_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver -kill :1
echo "🛑 Servidor VNC encerrado."
""",

    "run_sap.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux/sap_organizador
source ../venv/bin/activate
export DISPLAY=:1
python main.py
cd ~/downloads/s-ponto-termux
echo "✅ Programa finalizado. Você voltou para a pasta do projeto."
""",

    "git_push.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux
git add .
echo "Digite a mensagem do commit:"
read mensagem
git commit -m "$mensagem"
git push
echo "✅ Código enviado para o GitHub!"
""",

    "README.md": """# 🟣 S-Ponto Termux Kit

Este pacote contém scripts para facilitar a execução e manutenção do sistema S-Ponto no Termux com interface gráfica via VNC.

## ✅ Scripts incluídos

- `start_vnc.sh`: Inicia o servidor VNC no display :1
- `stop_vnc.sh`: Encerra o servidor VNC
- `run_sap.sh`: Ativa o ambiente virtual e executa o sistema com Tkinter
- `git_push.sh`: Faz commit e envia o projeto para o GitHub
- `README.md`: Este manual de uso

## 🧭 Como usar

### 1. Inicie o VNC:
```bash
./start_vnc.sh
import os
from zipfile import ZipFile

# Diretório temporário para montar os arquivos
base_dir = "/mnt/data/s-ponto-termux-kit"
os.makedirs(base_dir, exist_ok=True)

# Scripts e conteúdo do README
arquivos = {
    "start_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver :1
echo
echo "✅ VNC iniciado no display :1 (porta 5901)"
echo "Use o VNC Viewer e conecte-se ao endereço: 127.0.0.1:5901"
""",

    "stop_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver -kill :1
echo "🛑 Servidor VNC encerrado."
""",

    "run_sap.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux/sap_organizador
source ../venv/bin/activate
export DISPLAY=:1
python main.py
cd ~/downloads/s-ponto-termux
echo "✅ Programa finalizado. Você voltou para a pasta do projeto."
""",

    "git_push.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux
git add .
echo "Digite a mensagem do commit:"
read mensagem
git commit -m "$mensagem"
git push
echo "✅ Código enviado para o GitHub!"
""",

    "README.md": """# 🟣 S-Ponto Termux Kit

Este pacote contém scripts para facilitar a execução e manutenção do sistema S-Ponto no Termux com interface gráfica via VNC.

## ✅ Scripts incluídos

- `start_vnc.sh`: Inicia o servidor VNC no display :1
- `stop_vnc.sh`: Encerra o servidor VNC
- `run_sap.sh`: Ativa o ambiente virtual e executa o sistema com Tkinter
- `git_push.sh`: Faz commit e envia o projeto para o GitHub
- `README.md`: Este manual de uso

## 🧭 Como usar

### 1. Inicie o VNC:
```bash
./start_vnc.sh
import os
from zipfile import ZipFile

# Diretório temporário para montar os arquivos
base_dir = "/mnt/data/s-ponto-termux-kit"
os.makedirs(base_dir, exist_ok=True)

# Scripts e conteúdo do README
arquivos = {
    "start_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver :1
echo
echo "✅ VNC iniciado no display :1 (porta 5901)"
echo "Use o VNC Viewer e conecte-se ao endereço: 127.0.0.1:5901"
""",

    "stop_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver -kill :1
echo "🛑 Servidor VNC encerrado."
""",

    "run_sap.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux/sap_organizador
source ../venv/bin/activate
export DISPLAY=:1
python main.py
cd ~/downloads/s-ponto-termux
echo "✅ Programa finalizado. Você voltou para a pasta do projeto."
""",

    "git_push.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux
git add .
echo "Digite a mensagem do commit:"
read mensagem
git commit -m "$mensagem"
git push
echo "✅ Código enviado para o GitHub!"
""",

    "README.md": """# 🟣 S-Ponto Termux Kit

Este pacote contém scripts para facilitar a execução e manutenção do sistema S-Ponto no Termux com interface gráfica via VNC.

## ✅ Scripts incluídos

- `start_vnc.sh`: Inicia o servidor VNC no display :1
- `stop_vnc.sh`: Encerra o servidor VNC
- `run_sap.sh`: Ativa o ambiente virtual e executa o sistema com Tkinter
- `git_push.sh`: Faz commit e envia o projeto para o GitHub
- `README.md`: Este manual de uso

## 🧭 Como usar

### 1. Inicie o VNC:
```bash
./start_vnc.sh
import os
from zipfile import ZipFile

# Diretório temporário para montar os arquivos
base_dir = "/mnt/data/s-ponto-termux-kit"
os.makedirs(base_dir, exist_ok=True)

# Scripts e conteúdo do README
arquivos = {
    "start_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver :1
echo
echo "✅ VNC iniciado no display :1 (porta 5901)"
echo "Use o VNC Viewer e conecte-se ao endereço: 127.0.0.1:5901"
""",

    "stop_vnc.sh": """#!/data/data/com.termux/files/usr/bin/bash

vncserver -kill :1
echo "🛑 Servidor VNC encerrado."
""",

    "run_sap.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux/sap_organizador
source ../venv/bin/activate
export DISPLAY=:1
python main.py
cd ~/downloads/s-ponto-termux
echo "✅ Programa finalizado. Você voltou para a pasta do projeto."
""",

    "git_push.sh": """#!/data/data/com.termux/files/usr/bin/bash

cd ~/downloads/s-ponto-termux
git add .
echo "Digite a mensagem do commit:"
read mensagem
git commit -m "$mensagem"
git push
echo "✅ Código enviado para o GitHub!"
""",

    "README.md": """# 🟣 S-Ponto Termux Kit

Este pacote contém scripts para facilitar a execução e manutenção do sistema S-Ponto no Termux com interface gráfica via VNC.

## ✅ Scripts incluídos

- `start_vnc.sh`: Inicia o servidor VNC no display :1
- `stop_vnc.sh`: Encerra o servidor VNC
- `run_sap.sh`: Ativa o ambiente virtual e executa o sistema com Tkinter
- `git_push.sh`: Faz commit e envia o projeto para o GitHub
- `README.md`: Este manual de uso

## 🧭 Como usar

### 1. Inicie o VNC:
```bash
./start_vnc.sh
