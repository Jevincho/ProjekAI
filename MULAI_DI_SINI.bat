@echo off
setlocal

set "INNER_SCRIPT=%~dp0ProyekAI\SETUP_DAN_JALANKAN_WEB.bat"

if not exist "%INNER_SCRIPT%" (
    echo ERROR: File launcher utama tidak ditemukan:
    echo "%INNER_SCRIPT%"
    echo.
    pause
    exit /b 1
)

call "%INNER_SCRIPT%"
