# Instrucciones para Crear una Cuenta y Obtener un Subdominio Gratuito en Cloudflare

Este documento te guiará paso a paso para crear una cuenta en Cloudflare y obtener un subdominio gratuito.

## Paso 1: Crear una Cuenta en Cloudflare

1. **Visita el sitio web de Cloudflare**:
   - Abre tu navegador web y ve a [Cloudflare](https://www.cloudflare.com/).

2. **Regístrate**:
   - Haz clic en el botón **Sign Up** (Registrarse) en la esquina superior derecha.
   - Ingresa tu dirección de correo electrónico y una contraseña segura.
   - Acepta los términos de servicio y haz clic en **Create Account** (Crear cuenta).

3. **Confirma tu Correo Electrónico**:
   - Revisa tu bandeja de entrada y busca un correo electrónico de Cloudflare para confirmar tu dirección de correo electrónico.
   - Haz clic en el enlace de confirmación en el correo.

## Paso 2: Crear un Subdominio Gratuito

### Usar Cloudflare Workers para Crear un Subdominio

1. **Acceder al Panel de Control**:
   - Inicia sesión en tu cuenta de Cloudflare.

2. **Agregar un Sitio**:
   - Haz clic en **Add a Site** (Agregar un sitio).
   - Introduce un nombre de subdominio, por ejemplo, `tusubdominio.cloudflareworkers.com`. (Ten en cuenta que debes usar un nombre único y que no esté en uso).
   - Haz clic en **Add Site** (Agregar sitio).

3. **Seleccionar un Plan**:
   - Selecciona el plan gratuito y haz clic en **Confirm Plan** (Confirmar plan).

4. **Configurar el Subdominio**:
   - Cloudflare te proporcionará configuraciones de DNS. Puedes omitir esta parte si solo deseas usar Cloudflare Workers.
   - Haz clic en **Continue** (Continuar) para avanzar.

5. **Crear un Worker**:
   - En el panel de control de Cloudflare, ve a la sección **Workers**.
   - Haz clic en **Create a Service** (Crear un servicio).
   - Asigna un nombre a tu worker y haz clic en **Next** (Siguiente).

6. **Configurar el Worker**:
   - Puedes usar el editor en línea para escribir código o simplemente usar la plantilla predeterminada.
   - Haz clic en **Save and Deploy** (Guardar y desplegar) para activar tu worker.

7. **Asignar un Subdominio al Worker**:
   - Después de crear el worker, ve a la sección **Settings** (Configuraciones) del worker.
   - Busca la opción **Triggers** (Disparadores) y selecciona **Add Route** (Agregar ruta).
   - Escribe el subdominio que deseas usar, por ejemplo, `tusubdominio.cloudflareworkers.com/*`.
   - Haz clic en **Save** (Guardar).

## Paso 3: Obtener el API Token (Opcional)

Si planeas usar la API de Cloudflare para automatizar tareas, puedes crear un API Token.

1. **Acceder a Mi Perfil**:
   - En el panel de Cloudflare, haz clic en tu perfil en la esquina superior derecha y selecciona **My Profile** (Mi perfil).

2. **Crear un API Token**:
   - Ve a la pestaña **API Tokens**.
   - Haz clic en **Create Token** (Crear token).
   - Selecciona **Edit Cloudflare Workers** o crea un token personalizado con los permisos necesarios.
   - Haz clic en **Continue to summary** (Continuar al resumen) y luego en **Create Token** (Crear token).
   - Guarda el token en un lugar seguro.

## Conclusión

Ahora has creado una cuenta en Cloudflare y obtenido un subdominio gratuito utilizando Cloudflare Workers. Puedes usar este subdominio para tus aplicaciones y servicios.

Si tienes más preguntas o necesitas ayuda adicional, ¡no dudes en preguntar!
