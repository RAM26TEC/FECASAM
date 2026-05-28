# 🚀 Guía de Despliegue en Hostinger

Esta guía te llevará paso a paso para desplegar FECASAM 2026 en Hostinger.

## 📋 Pre-requisitos

- [ ] Cuenta de Hostinger activa
- [ ] Dominio registrado o subdominio configurado
- [ ] Acceso a cPanel
- [ ] Cliente FTP (FileZilla) instalado
- [ ] Archivos del proyecto descargados

## 🎯 Paso 1: Acceder a Hostinger

1. Ve a [hostinger.com](https://www.hostinger.com)
2. Inicia sesión en tu cuenta
3. En el panel de control, selecciona tu hosting
4. Haz clic en **"Administrar"**

## 🗄️ Paso 2: Crear Base de Datos

### 2.1 Crear la Base de Datos

1. En cPanel, busca **"MySQL Databases"** o **"Bases de datos MySQL"**
2. En **"Create New Database"**, ingresa: `fecasam2026`
3. Haz clic en **"Create Database"**

### 2.2 Crear Usuario de Base de Datos

1. En la misma página, ve a **"MySQL Users"**
2. Crea un nuevo usuario:
   - **Username:** `fecasam_admin`
   - **Password:** Genera una contraseña segura (guárdala)
3. Haz clic en **"Create User"**

### 2.3 Asignar Usuario a Base de Datos

1. En **"Add User to Database"**, selecciona:
   - **User:** `fecasam_admin`
   - **Database:** `fecasam2026`
2. Haz clic en **"Add"**
3. En permisos, marca **"ALL PRIVILEGES"**
4. Haz clic en **"Make Changes"**

### 2.4 Importar Esquema de Base de Datos

1. Ve a **cPanel > phpMyAdmin**
2. Selecciona la base de datos `fecasam2026` en el panel izquierdo
3. Haz clic en la pestaña **"Import"**
4. Selecciona el archivo `database/schema.sql`
5. Haz clic en **"Go"**
6. Verifica que las tablas se hayan creado correctamente

## 📁 Paso 3: Configurar Archivos PHP

### 3.1 Editar submit-registration.php

Abre `api/submit-registration.php` y actualiza:

```php
define('DB_HOST', 'localhost');
define('DB_NAME', 'tunombre_fecasam2026'); // Formato: usuario_nombredb
define('DB_USER', 'tunombre_fecasam_admin');
define('DB_PASS', 'tu_contraseña_aqui');
define('ADMIN_EMAIL', 'info@tudominio.com');
```

**Nota:** Hostinger usa el formato `usuario_nombredb` y `usuario_user` para bases de datos.

### 3.2 Editar submit-complaint.php

Crea el archivo si no existe, copiando la misma estructura de `submit-registration.php` pero adaptado para la tabla `complaints`.

## 🌐 Paso 4: Subir Archivos al Servidor

### Opción A: File Manager (Recomendado para principiantes)

1. En cPanel, abre **"File Manager"**
2. Navega a la carpeta `public_html`
3. Si hay archivos de ejemplo, elimínalos o muévelos a otra carpeta
4. Haz clic en **"Upload"** en la barra superior
5. Sube TODOS los archivos del proyecto
6. Verifica que la estructura sea correcta:

```
public_html/
├── index.html
├── libro-reclamaciones.html
├── 404.html
├── .htaccess
├── assets/
├── api/
└── ...
```

### Opción B: FTP (Más rápido para archivos grandes)

1. Abre FileZilla
2. Obtén tus credenciales FTP:
   - **Host:** ftp.tudominio.com
   - **Username:** Tu usuario de cPanel
   - **Password:** Tu contraseña de cPanel
   - **Port:** 21

3. Conecta a tu servidor
4. En el panel remoto, navega a `public_html`
5. Arrastra todos los archivos del proyecto desde el panel local

### 4.1 Verificar Archivos Ocultos

1. En File Manager, haz clic en **"Settings"** (esquina superior derecha)
2. Marca **"Show Hidden Files (dotfiles)"**
3. Verifica que `.htaccess` esté presente

## 🔒 Paso 5: Configurar Permisos

### 5.1 Permisos de Archivos

En File Manager, selecciona todos los archivos y:

1. Haz clic derecho > **"Change Permissions"**
2. Establece los permisos según:

```
Directorios: 755
Archivos .html: 644
Archivos .php: 644
Archivos .css: 644
Archivos .js: 644
.htaccess: 644
```

### 5.2 Permisos Específicos

Para carpetas que necesitan escritura (si es necesario):

```bash
assets/downloads/: 755
api/temp/: 755 (si existe)
```

## 🔐 Paso 6: Configurar SSL (HTTPS)

### 6.1 Activar SSL Gratuito

1. En el panel de Hostinger, ve a **"SSL"**
2. Selecciona tu dominio
3. Haz clic en **"Install SSL"** (Let's Encrypt gratuito)
4. Espera unos minutos a que se active

### 6.2 Forzar HTTPS

En `.htaccess`, descomenta estas líneas:

```apache
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
```

## 📧 Paso 7: Configurar Email

### 7.1 Crear Cuenta de Email

1. En cPanel, ve a **"Email Accounts"**
2. Crea la cuenta: `inscripciones@tudominio.com`
3. Establece una contraseña segura

### 7.2 Actualizar Configuración

En todos los archivos PHP, actualiza:

```php
define('ADMIN_EMAIL', 'inscripciones@tudominio.com');
```

### 7.3 Verificar Función mail()

Crea un archivo `test-email.php`:

```php
<?php
$to = 'tu@email.com';
$subject = 'Test Email';
$message = 'Este es un email de prueba';
$headers = 'From: inscripciones@tudominio.com';

if(mail($to, $subject, $message, $headers)) {
    echo 'Email enviado exitosamente';
} else {
    echo 'Error al enviar email';
}
?>
```

Visita: `https://tudominio.com/test-email.php`

**Importante:** Elimina este archivo después de la prueba.

## 🌍 Paso 8: Configurar Dominio

### Si usas el dominio principal:

Ya está configurado automáticamente.

### Si usas un subdominio:

1. En cPanel, ve a **"Subdomains"**
2. Crea el subdominio: `fecasam.tudominio.com`
3. Establece la raíz del documento: `public_html/fecasam`
4. Mueve todos los archivos a esa carpeta

### Si usas un dominio externo (addon domain):

1. Actualiza los nameservers de tu dominio a los de Hostinger
2. En cPanel, ve a **"Addon Domains"**
3. Añade el dominio y configura la raíz del documento

## ✅ Paso 9: Verificar Instalación

### 9.1 Checklist de Verificación

- [ ] La página principal carga: `https://tudominio.com`
- [ ] No hay errores 404 en CSS/JS
- [ ] Las imágenes cargan correctamente
- [ ] El menú de navegación funciona
- [ ] Los smooth scrolls funcionan
- [ ] El formulario de inscripción se muestra
- [ ] El libro de reclamaciones carga
- [ ] Los botones flotantes aparecen

### 9.2 Probar Formulario de Inscripción

1. Llena el formulario con datos de prueba
2. Envía el formulario
3. Verifica:
   - ✅ Mensaje de éxito aparece
   - ✅ Email de confirmación llega
   - ✅ Datos se guardan en la base de datos (phpMyAdmin)

### 9.3 Verificar Base de Datos

1. Ve a **phpMyAdmin**
2. Selecciona `fecasam2026`
3. Haz clic en `registrations`
4. Verifica que tu registro de prueba esté ahí

## 🔧 Paso 10: Configuración Avanzada (Opcional)

### 10.1 Optimización de PHP

En cPanel, busca **"Select PHP Version"** o **"PHP Selector"**:

```
PHP Version: 8.0 o superior
upload_max_filesize: 64M
post_max_size: 64M
max_execution_time: 300
memory_limit: 256M
```

### 10.2 Configurar Caché

En `.htaccess`, las reglas de caché ya están configuradas.

### 10.3 Habilitar Compresión

La compresión GZIP ya está habilitada en `.htaccess`.

## 📊 Paso 11: Analytics y Monitoreo

### 11.1 Google Analytics

1. Crea una cuenta en [analytics.google.com](https://analytics.google.com)
2. Crea una propiedad para tu sitio
3. Copia el código de seguimiento
4. Añádelo en `index.html` antes de `</head>`

### 11.2 Google Search Console

1. Ve a [search.google.com/search-console](https://search.google.com/search-console)
2. Añade tu propiedad
3. Verifica la propiedad (método recomendado: DNS)
4. Envía tu sitemap: `https://tudominio.com/sitemap.xml`

## 🐛 Solución de Problemas Comunes

### Error: Internal Server Error (500)

**Causa:** Problema en `.htaccess`

**Solución:**
1. Renombra `.htaccess` a `.htaccess.bak`
2. Si el sitio carga, el problema está en `.htaccess`
3. Revisa línea por línea o contacta soporte de Hostinger

### Error: Base de datos no conecta

**Causa:** Credenciales incorrectas

**Solución:**
1. Verifica el formato: `usuario_nombredb`
2. Verifica la contraseña en `api/submit-registration.php`
3. Prueba la conexión con `test-connection.php`:

```php
<?php
$conn = new PDO("mysql:host=localhost;dbname=usuario_fecasam2026", "usuario_fecasam_admin", "password");
echo "Conexión exitosa";
?>
```

### Error: CSS/JS no cargan

**Causa:** Rutas incorrectas o permisos

**Solución:**
1. Verifica que las rutas en HTML sean correctas
2. Verifica permisos (644 para archivos)
3. Limpia caché del navegador (Ctrl + F5)

### Emails no llegan

**Causa:** SPF/DKIM no configurados

**Solución:**
1. Verifica que uses email del mismo dominio
2. En cPanel > Email Deliverability, verifica SPF y DKIM
3. Revisa la carpeta de spam
4. Considera usar SMTP externo (Gmail, SendGrid)

## 📝 Paso 12: Mantenimiento Post-Instalación

### 12.1 Cambiar Contraseña de Admin

```sql
-- En phpMyAdmin, ejecuta:
UPDATE admin_users 
SET password_hash = '$2y$10$TU_HASH_AQUI' 
WHERE username = 'admin';
```

Genera el hash en: [bcrypt-generator.com](https://bcrypt-generator.com/)

### 12.2 Configurar Backup Automático

Hostinger Premium incluye backups automáticos semanales.

Para backups adicionales:

1. Ve a **cPanel > Backup**
2. Descarga backup completo
3. Guárdalo en un lugar seguro

### 12.3 Actualizar Contenido

Edita `index.html` para:
- Cambiar imágenes
- Actualizar textos
- Modificar fechas
- Añadir/quitar secciones

## 📞 Soporte Hostinger

Si tienes problemas:

- 💬 Chat 24/7 en Hostinger
- 📧 Soporte via tickets
- 📚 Base de conocimientos: [hostinger.com/tutorials](https://www.hostinger.com/tutorials)

## ✅ Checklist Final

- [ ] Base de datos creada e importada
- [ ] Archivos subidos correctamente
- [ ] Permisos configurados
- [ ] SSL activado y forzado
- [ ] Email configurado y funcionando
- [ ] Formularios probados
- [ ] Google Analytics añadido
- [ ] Sitemap enviado a Google
- [ ] Contraseñas de admin cambiadas
- [ ] Backup inicial creado

## 🎉 ¡Felicitaciones!

Tu sitio FECASAM 2026 está ahora en vivo. 

Visita: **https://tudominio.com**

---

**¿Necesitas ayuda?** Consulta el README.md principal o contacta al equipo de desarrollo.
