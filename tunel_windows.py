#!/usr/bin/env python3
import subprocess
import sys
import os
import re
import argparse
from threading import Thread
from queue import Queue
import platform

def run_cloudflared(ip, port, queue):
    """
    Ejecuta cloudflared y captura la URL
    """
    exe = "cloudflared.exe" if os.name == "nt" else "./cloudflared"
    cmd = f"{exe} tunnel --url http://{ip}:{port}"
    process = subprocess.Popen(
        cmd.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
    )

    url_pattern = re.compile(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com')

    for line in process.stdout:
        match = url_pattern.search(line)
        if match:
            queue.put(match.group(0))
            break

def download_cloudflared():
    """Descarga cloudflared según el sistema operativo"""
    print("Descargando cloudflared...")
    system = platform.system().lower()
    if system == "windows":
        url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
        exe_name = "cloudflared.exe"
        # Usar PowerShell para descargar si curl no está disponible
        try:
            subprocess.run(f"curl -L {url} -o {exe_name}", shell=True, check=True)
        except Exception:
            subprocess.run(f"powershell -Command \"Invoke-WebRequest -Uri {url} -OutFile {exe_name}\"", shell=True, check=True)
    else:
        arch = platform.machine()
        arch = "arm64" if arch in ["aarch64", "arm64"] else "amd64"
        url = f"https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-{arch}"
        subprocess.run(f"wget {url} -O cloudflared && chmod +x cloudflared", shell=True, check=True)

def main():
    parser = argparse.ArgumentParser(
        description='Crear túnel Cloudflare para exponer servidores locales',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Ejemplos:
  python tunel-closflare.py -p 8080
  python tunel-closflare.py -i 192.168.1.100 -p 3000 --download
  python tunel-closflare.py --help""")

    parser.add_argument('-i', '--ip', default='localhost',
                      help='IP del servidor local (default: localhost)')
    parser.add_argument('-p', '--port', required=True, type=int,
                      help='Puerto local a exponer (requerido)')
    parser.add_argument('--download', action='store_true',
                      help='Descargar cloudflared automáticamente si no existe')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0',
                      help='Mostrar versión del programa')

    args = parser.parse_args()

    exe = "cloudflared.exe" if os.name == "nt" else "./cloudflared"
    if not os.path.exists(exe):
        if args.download:
            download_cloudflared()
        else:
            print("Error: cloudflared no encontrado. Usa --download para instalarlo automáticamente")
            sys.exit(1)

    print(f"\nIniciando túnel para http://{args.ip}:{args.port}")

    url_queue = Queue()
    thread = Thread(target=run_cloudflared, args=(args.ip, args.port, url_queue))
    thread.daemon = True
    thread.start()

    try:
        public_url = url_queue.get(timeout=30)
        print("\n\033[1;32mTúnel creado exitosamente!\033[0m")
        print(f"\033[1;34mURL pública: {public_url}\033[0m")
        print("\nPresiona Ctrl+C para detener el túnel")
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