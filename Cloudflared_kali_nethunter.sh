#!/bin/bash
# cloudflared_aarch64.sh - Túnel con Cloudflare para dispositivos ARM64 (aarch64)

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar arquitectura
ARCH=$(uname -m)
if [ "$ARCH" != "aarch64" ]; then
    echo -e "${RED}Error: Este script es solo para arquitectura aarch64${NC}"
    echo -e "Tu arquitectura es: ${YELLOW}$ARCH${NC}"                     exit 1
fi

# Instalar dependencias
echo -e "${YELLOW}Instalando dependencias...${NC}"
sudo apt update
sudo apt install -y wget                                              
# Descargar cloudflared para ARM64
echo -e "${YELLOW}Descargando cloudflared para aarch64...${NC}"
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared
chmod +x cloudflared

# Configurar (opcional)
echo -e "${GREEN}Configuración opcional:${NC}"
read -p "¿Quieres autenticar con tu cuenta Cloudflare? (s/n): " auth_choice
if [ "$auth_choice" = "s" ] || [ "$auth_choice" = "S" ]; then
    ./cloudflared login
fi

# Iniciar túnel
echo -e "${YELLOW}Iniciando túnel...${NC}"                            echo -e "${GREEN}Ingresa el puerto local a exponer (ej: 8080):${NC} "
read port

./cloudflared tunnel --url http://localhost:$port

# Opción alternativa si falla:
# ./cloudflared tunnel --hostname tunel.example.com --url http://localhost:$port
