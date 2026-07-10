#!/bin/bash

APP_URL="http://127.0.0.1:5000"

echo ""
echo "============================================================"
echo "  Rembg-Fuse Web App Launcher"
echo "============================================================"
echo ""

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: Python 3 tidak ditemukan."
    echo "Install Python dari https://www.python.org/downloads/"
    exit 1
fi

echo "Mengecek Python..."
python3 --version || exit 1

echo ""
echo "Install dependencies tanpa virtual environment..."
python3 -m pip install --upgrade pip --user || exit 1
python3 -m pip install -r web_app/requirements.txt --user || exit 1

echo ""
echo "============================================================"
echo "  Aplikasi berjalan di:"
echo "  $APP_URL"
echo ""
echo "  Tekan CTRL + C untuk menghentikan server."
echo "============================================================"
echo ""

python3 -m flask --app web_app.app run --debug
