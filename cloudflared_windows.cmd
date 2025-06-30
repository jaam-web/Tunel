@echo off
REM cloudflared_windows.cmd - Túnel con Cloudflare para Windows

REM Colores
set RED=0C
set GREEN=0A
set YELLOW=0E
set NC=07

REM Verificar arquitectura
for /f "tokens=2 delims==" %%i in ('wmic os get osarchitecture /format:list') do set ARCH=%%i
if not "%ARCH%"=="64-bit" (
    echo.
    echo %RED%Error: Este script es solo para arquitectura de 64 bits%NC%
    echo Tu arquitectura es: %YELLOW%%ARCH%%NC%
    exit /b 1
)

REM Instalar dependencias
echo.
echo %YELLOW%Instalando dependencias...%NC%
REM Nota: Asegúrate de tener Chocolatey instalado para poder usar wget
choco install -y wget

REM Descargar cloudflared para Windows
echo.
echo %YELLOW%Descargando cloudflared para Windows...%NC%
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe -O cloudflared.exe

REM Configurar (opcional)
echo.
echo %GREEN%Configuración opcional:%NC%
set /p auth_choice="¿Quieres autenticar con tu cuenta Cloudflare? (s/n): "
if /i "%auth_choice%"=="s" (
    cloudflared.exe login
)

REM Iniciar túnel
echo.
echo %YELLOW%Iniciando túnel...%NC%
set /p port="Ingresa el puerto local a exponer (ej: 8080): "

cloudflared.exe tunnel --url http://localhost:%port%

REM Opción alternativa si falla:
REM cloudflared.exe tunnel --hostname tunel.example.com --url http://localhost:%port%
