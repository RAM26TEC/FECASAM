# 🚀 Guía de Inicio Rápido

¡Bienvenido a FECASAM 2026! Esta guía te ayudará a poner en marcha el sitio web en **15 minutos**.

## ⚡ Inicio Rápido (3 pasos)

### 1️⃣ Preparar Archivos (2 min)

```bash
# Descarga el proyecto
# Asegúrate de tener todos los archivos en una carpeta
```

### 2️⃣ Configurar Base de Datos (5 min)

1. Accede a **cPanel → phpMyAdmin**
2. Crea base de datos: `fecasam2026`
3. Importa: `database/schema.sql`
4. Anota tus credenciales

### 3️⃣ Subir y Configurar (8 min)

1. Sube archivos a `public_html/`
2. Edita `api/submit-registration.php`:
   ```php
   define('DB_NAME', 'tu_usuario_fecasam2026');
   define('DB_USER', 'tu_usuario_fecasam_admin');
   define('DB_PASS', 'tu_contraseña');
   ```
3. ¡Listo! Visita tu sitio

## 📋 Checklist Mínimo

- [ ] PHP 7.4+ instalado
- [ ] MySQL/MariaDB activo
- [ ] Dominio apuntando al servidor
- [ ] Base de datos creada
- [ ] Archivos subidos a `public_html/`
- [ ] Credenciales configuradas
- [ ] `.htaccess` presente

## 🎯 Verificación Rápida

Visita estos URLs para verificar:

```
✅ https://tudominio.com/ - Página principal
✅ https://tudominio.com/libro-reclamaciones.html - Libro
✅ Prueba el formulario de inscripción
```

## 🔧 Configuración Básica vs Completa

### Básica (15 min) ⚡
- Base de datos
- Archivos subidos
- Configuración PHP
- **Listo para usar**

### Completa (1-2 horas) 🎨
- Todo lo básico +
- SSL configurado
- Emails funcionando
- Imágenes optimizadas
- PDFs subidos
- Analytics conectado
- Backup configurado

## 📞 ¿Problemas?

### Error 500
→ Revisa `.htaccess` (renómbralo temporalmente)

### No carga CSS/JS
→ Verifica rutas y permisos (644)

### Formulario no funciona
→ Revisa credenciales de BD en PHP

## 📖 Documentación Completa

- **README.md** - Documentación general
- **DEPLOYMENT.md** - Guía paso a paso
- **RECURSOS-NECESARIOS.md** - Lista de assets

## ✨ ¡Ya está!

Tu sitio debería estar funcionando. Ahora puedes:

1. Personalizar contenido en `index.html`
2. Subir tus imágenes a `assets/images/`
3. Añadir PDFs a `assets/downloads/`
4. Configurar SSL (Hostinger lo hace automático)
5. Conectar Google Analytics

---

**¿Todo funcionó?** ¡Excelente! Pasa a la configuración completa.

**¿Tuviste problemas?** Consulta DEPLOYMENT.md o contacta soporte.
