@echo off
setlocal
title Rembg-Fuse Web App

set "APP_URL=http://127.0.0.1:5000"
set "VENV_DIR=%~dp0venv"
set "VENV_PYTHON=%VENV_DIR%\Scripts\python.exe"
set "VENV_ACTIVATE=%VENV_DIR%\Scripts\activate.bat"
set "SETUP_MARKER=%VENV_DIR%\.setup_done"

echo.
echo ============================================================
echo   Rembg-Fuse Web App Launcher
echo ============================================================
echo.

where py >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_CMD=py -3"
) else (
    where python >nul 2>nul
    if not errorlevel 1 (
        set "PYTHON_CMD=python"
    ) else (
        echo ERROR: Python tidak ditemukan.
        echo Install Python dari https://www.python.org/downloads/
        echo Saat install, centang "Add Python to PATH".
        echo.
        pause
        exit /b 1
    )
)

echo Mengecek Python...
%PYTHON_CMD% --version
if errorlevel 1 (
    echo.
    echo ERROR: Python gagal dijalankan.
    pause
    exit /b 1
)

echo.
if not exist "%VENV_PYTHON%" (
    echo Membuat virtual environment...
    %PYTHON_CMD% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo.
        echo ERROR: Gagal membuat virtual environment.
        pause
        exit /b 1
    )
)

if not exist "%VENV_ACTIVATE%" (
    echo.
    echo ERROR: File activate.bat tidak ditemukan:
    echo "%VENV_ACTIVATE%"
    pause
    exit /b 1
)

echo Mengaktifkan virtual environment...
call "%VENV_ACTIVATE%"
if errorlevel 1 (
    echo.
    echo ERROR: Gagal mengaktifkan virtual environment.
    pause
    exit /b 1
)

if not exist "%SETUP_MARKER%" (
    echo.
    echo Install dependencies...
    python -m pip install --upgrade pip
    if errorlevel 1 (
        echo.
        echo ERROR: Gagal update pip.
        pause
        exit /b 1
    )

    python -m pip install -r web_app\requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: Gagal install dependencies.
        echo Coba cek koneksi internet, lalu jalankan lagi.
        pause
        exit /b 1
    )

    echo setup complete>"%SETUP_MARKER%"
) else (
    echo.
    echo Dependencies sudah pernah di-install. Melewati step install.
)

echo.
echo ============================================================
echo   Aplikasi berjalan di:
echo   %APP_URL%
echo.
echo   Tekan CTRL + C untuk menghentikan server.
echo ============================================================
echo.

start "" "%APP_URL%"
python -m flask --app web_app.app run --debug

echo.
echo Server berhenti.
pause
