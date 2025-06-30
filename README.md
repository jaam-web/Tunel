# tunel_windosw.py

Este script permite exponer un servidor local a Internet utilizando Cloudflare Tunnel (cloudflared) de forma sencilla, compatible con **Windows** y **Linux**.

## Requisitos

- Python 3.x
- [cloudflared](https://github.com/cloudflare/cloudflared) (el script puede descargarlo automáticamente)
- Acceso a Internet

## Instalación

1. Descarga el script `tunel_windosw.py` a una carpeta de tu preferencia.
2. (Opcional) Descarga manualmente el binario de `cloudflared` desde [aquí](https://github.com/cloudflare/cloudflared/releases) y colócalo en la misma carpeta, o usa la opción `--download` para que el script lo descargue automáticamente.

## Uso

Abre una terminal (CMD, PowerShell o Terminal de VS Code) y navega a la carpeta donde está el script.

### Ejemplos de ejecución

Exponer el puerto 8080 de tu máquina local:
```sh
python tunel_windosw.py -p 8080
```

Exponer el puerto 3000 de una IP local específica y descargar cloudflared si no existe:
```sh
python tunel_windosw.py -i 192.168.1.100 -p 3000 --download
```

Mostrar la ayuda:
```sh
python tunel_windosw.py --help
```

## Argumentos

- `-i`, `--ip`  
  IP del servidor local a exponer (por defecto: `localhost`).

- `-p`, `--port`  
  Puerto local a exponer (**requerido**).

- `--download`  
  Descarga automáticamente el binario de cloudflared si no está presente.

- `--version`  
  Muestra la versión del script.

## Salida

Si el túnel se crea correctamente, verás una URL pública similar a:

```
Túnel creado exitosamente!
URL pública: https://xxxxxxx.trycloudflare.com
Presiona Ctrl+C para detener el túnel
```

## Notas

- En Windows, el binario debe llamarse `cloudflared.exe`.
- El túnel permanecerá activo hasta que detengas el script con `Ctrl+C`.
- Si tienes problemas con la descarga automática, puedes descargar `cloudflared` manualmente y colocarlo junto al script.

---
Desarrollado para fines educativos.
