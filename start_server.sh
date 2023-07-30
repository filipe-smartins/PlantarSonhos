#!/bin/bash
chmod +x "$0"  # Torna o próprio script executável
echo "Iniciando o sistema, por favor aguarde..."
python3 manage.py runserver
sleep 15
xdg-open http://127.0.0.1:8000/
