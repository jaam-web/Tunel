#!/usr/bin/env python3
import subprocess
import sys
import os
import re
from threading import Thread
from queue import Queue

def run_cloudflared(ip, port, queue):
    """
    Ejecuta cloudflared y captura la URL
    """
    cmd = f"./cloudflared tunnel --url http://{ip}:{port}"
    process = subprocess.Popen(
        cmd.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    
    url_pattern = re.compile(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com')
    
    for line in process.stdout:
        match = url_pattern.search(line)
        if match:
            queue.put(match.group(0))
            break

def main():
    # Verificar si cloudflared está instalado
    if not os.path.exists("./cloudflared"):
        print("Descargando cloudflared...")
        arch = os.uname().machine
        url = f"https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-{'arm64' if arch == 'aarch64' else 'amd64'}"
        subprocess.run(f"wget {url} -O cloudflared && chmod +x cloudflared", shell=True, check=True)
    
    # Obtener parámetros
    print("python3 tunel.py")
    ip = input("Ingrese la IP del servidor local [localhost]: ") or "localhost"
    port = input("Ingrese el puerto local [8080]: ") or "8080"
    
    print(f"\nIniciando túnel para http://{ip}:{port}")
    
    # Cola para capturar la URL
    url_queue = Queue()
    
    # Hilo para ejecutar cloudflared
    thread = Thread(target=run_cloudflared, args=(ip, port, url_queue))
    thread.daemon = True
    thread.start()
    
    try:
        # Esperar máximo 30 segundos por la URL
        public_url = url_queue.get(timeout=30)
        print("\n\033[1;32mTúnel creado exitosamente!\033[0m")
        print(f"\033[1;34mURL pública: {public_url}\033[0m")
        print("\nPresiona Ctrl+C para detener el túnel")
        
        # Mantener el programa corriendo
        while True:
            pass
    except:
        print("\n\033[1;31mError: No se pudo obtener la URL del túnel\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTúnel detenido")
        sys.exit(0)
