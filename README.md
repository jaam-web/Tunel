# Instrucciones para Crear una Cuenta y un Dominio Gratuito en Cloudflare

Este documento te guiará paso a paso para crear una cuenta en Cloudflare y obtener un dominio gratuito.

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

## Paso 2: Obtener un Dominio Gratuito

### Opción 1: Usar un Dominio Gratuito de Freenom

1. **Visita Freenom**:
   - Abre una nueva pestaña y ve a [Freenom](https://www.freenom.com/).

2. **Buscar un Dominio**:
   - En la página principal, busca un nombre de dominio que te gustaría registrar.
   - Asegúrate de seleccionar una extensión gratuita como `.tk`, `.ml`, `.ga`, `.cf`, o `.gq`.

3. **Registrar el Dominio**:
   - Una vez que encuentres un dominio disponible, haz clic en **Get it Now** (Consíguelo ahora).
   - Haz clic en **Checkout** (Pagar) para proceder.

4. **Crear una Cuenta en Freenom**:
   - Si no tienes una cuenta en Freenom, se te pedirá que crees una. Completa el formulario con tu información.
   - Acepta los términos y condiciones y haz clic en **Complete Order** (Completar pedido).

5. **Configurar el Dominio**:
   - Ve a **My Domains** (Mis dominios) en Freenom.
   - Haz clic en **Manage Domain** (Administrar dominio) junto al dominio que registraste.
   - Ve a la pestaña **Management Tools** (Herramientas de gestión) y selecciona **Nameservers** (Servidores de nombres).
   - Cambia a **Use custom nameservers** (Usar servidores de nombres personalizados) e ingresa los servidores de nombres de Cloudflare (los obtendrás en el siguiente paso).

### Opción 2: Usar un Dominio de Cloudflare (si ya tienes uno)

Si ya tienes un dominio registrado en otro lugar, puedes usarlo en Cloudflare. Solo necesitarás cambiar los servidores de nombres en tu registrador para que apunten a Cloudflare.

## Paso 3: Agregar el Dominio a Cloudflare

1. **Volver a Cloudflare**:
   - Regresa a la pestaña de Cloudflare y haz clic en **Add a Site** (Agregar un sitio).

2. **Ingresar el Dominio**:
   - Escribe el dominio que registraste (por ejemplo, `tudominio.tk`) y haz clic en **Add Site** (Agregar sitio).

3. **Seleccionar un Plan**:
   - Selecciona el plan gratuito y haz clic en **Confirm Plan** (Confirmar plan).

4. **Configurar los Servidores de Nombres**:
   - Cloudflare te proporcionará dos servidores de nombres. Copia esta información.
   - Regresa a Freenom y pega los servidores de nombres en la sección de **Nameservers**.

5. **Finalizar la Configuración**:
   - Haz clic en **Change Nameservers** (Cambiar servidores de nombres) en Freenom.
   - Regresa a Cloudflare y haz clic en **Done, Check Nameservers** (Listo, verificar servidores de nombres).

6. **Esperar la Propagación**:
   - Puede tardar unos minutos en propagarse. Una vez que Cloudflare confirme que los servidores de nombres están configurados correctamente, podrás usar tu dominio.

## Paso 4: Obtener el API Token

1. **Acceder a Mi Perfil**:
   - En el panel de Cloudflare, haz clic en tu perfil en la esquina superior derecha y selecciona **My Profile** (Mi perfil).

2. **Crear un API Token**:
   - Ve a la pestaña **API Tokens**.
   - Haz clic en **Create Token** (Crear token).
   - Selecciona **Edit Cloudflare Workers** o crea un token personalizado con los permisos necesarios (Zone.Zone, Zone.DNS, Account.Tunnel).
   - Haz clic en **Continue to summary** (Continuar al resumen) y luego en **Create Token** (Crear token).
   - Guarda el token en un lugar seguro.

## Conclusión

Ahora has creado una cuenta en Cloudflare, registrado un dominio gratuito y obtenido un API Token. Puedes usar esta información para configurar túneles y otros servicios en Cloudflare.

Si tienes más preguntas o necesitas ayuda adicional, ¡no dudes en preguntar!
