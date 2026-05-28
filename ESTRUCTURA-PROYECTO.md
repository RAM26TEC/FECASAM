# 📁 Estructura del Proyecto FECASAM 2026

```
FECASAM 2026/
│
├── 📄 index.html                       # Página principal
├── 📄 libro-reclamaciones.html         # Libro de reclamaciones virtual
├── 📄 404.html                         # Página de error 404
├── 📄 .htaccess                        # Configuración Apache/Hostinger
├── 📄 robots.txt                       # Instrucciones para bots
├── 📄 sitemap.xml                      # Mapa del sitio para SEO
├── 📄 .gitignore                       # Archivos ignorados por Git
│
├── 📘 README.md                        # Documentación principal
├── 📘 INICIO-RAPIDO.md                 # Guía de inicio rápido (15 min)
├── 📘 RECURSOS-NECESARIOS.md           # Checklist de recursos
├── 📘 project-context.md               # Contexto del proyecto original
│
├── 📂 assets/                          # Recursos del sitio
│   │
│   ├── 📂 css/
│   │   └── 📄 style.css               # Estilos principales (26KB comentado)
│   │
│   ├── 📂 js/
│   │   └── 📄 main.js                 # JavaScript principal (interactividad)
│   │
│   ├── 📂 images/                      # Imágenes del sitio
│   │   ├── 🖼️ logo.png               # Logo principal (NECESARIO)
│   │   ├── 🖼️ logo-light.png         # Logo claro (NECESARIO)
│   │   ├── 🖼️ favicon.png            # Favicon (NECESARIO)
│   │   ├── 🖼️ og-image.jpg           # Open Graph para redes sociales
│   │   ├── 🖼️ fibra-alpaca.jpg       # Imagen feature fibra
│   │   ├── 🖼️ carne-camelidos.jpg    # Imagen feature carne
│   │   └── 🖼️ banner.jpg             # Banner opcional
│   │
│   ├── 📂 videos/                      # Videos del sitio
│   │   └── 🎥 hero-alpacas.mp4        # Video hero (opcional)
│   │
│   └── 📂 downloads/                   # PDFs descargables
│       ├── 📑 programa-fecasam-2026.pdf
│       ├── 📑 bases-concurso.pdf
│       ├── 📑 ruta-paqochanan.pdf
│       ├── 📑 catalogo-expositores.pdf
│       └── 📑 manual-biotecnologia.pdf
│
├── 📂 api/                             # Backends PHP
│   ├── 📄 submit-registration.php     # Procesa inscripciones
│   └── 📄 submit-complaint.php        # Procesa reclamaciones (crear)
│
├── 📂 database/                        # Base de datos
│   └── 📄 schema.sql                  # Esquema completo MySQL
│
└── 📂 docs/                            # Documentación
    ├── 📄 DEPLOYMENT.md               # Guía paso a paso Hostinger
    └── 📄 MAINTENANCE.md              # Guía de mantenimiento (crear)
```

## 🎯 Archivos Críticos (No eliminar)

### HTML Principal
- `index.html` - Página principal con todas las secciones
- `libro-reclamaciones.html` - Formulario legal INDECOPI
- `404.html` - Página de error personalizada

### Configuración del Servidor
- `.htaccess` - Reglas de Apache (seguridad, compresión, caché)
- `robots.txt` - Control de crawlers
- `sitemap.xml` - SEO structure

### Estilos y Scripts
- `assets/css/style.css` - Todos los estilos (1 archivo)
- `assets/js/main.js` - Toda la funcionalidad JS

### Backend
- `api/submit-registration.php` - Endpoint inscripciones
- `database/schema.sql` - Estructura de BD

## 📦 Archivos a Crear/Personalizar

### 🔴 Prioridad Alta (Antes de producción)
```
assets/images/logo.png
assets/images/logo-light.png
assets/images/favicon.png
assets/downloads/*.pdf (al menos programa oficial)
```

### 🟡 Prioridad Media (Primeras semanas)
```
assets/images/fibra-alpaca.jpg
assets/images/carne-camelidos.jpg
assets/images/og-image.jpg
assets/videos/hero-alpacas.mp4
```

### 🟢 Prioridad Baja (Opcional)
```
api/submit-complaint.php (similar a registration)
docs/MAINTENANCE.md
403.html, 500.html (páginas de error adicionales)
```

## 🔧 Configuración Necesaria

### Antes de subir a producción:
1. **Base de datos:**
   - Importar `database/schema.sql`
   - Anotar credenciales

2. **PHP:**
   - Editar `api/submit-registration.php`
   - Actualizar DB_NAME, DB_USER, DB_PASS, ADMIN_EMAIL

3. **Dominio:**
   - Configurar DNS si es necesario
   - Activar SSL en Hostinger

4. **Emails:**
   - Crear cuenta `inscripciones@tudominio.com`
   - Verificar SPF/DKIM

## 📊 Tamaño Estimado del Proyecto

```
HTML/CSS/JS:        ~150 KB
Imágenes:           ~2-5 MB (optimizadas)
Videos:             ~10 MB (opcional)
PDFs:               ~5-15 MB
Base de datos:      ~100 KB (vacía)
─────────────────────────────
Total:              ~17-30 MB
```

## 🚀 Optimización para Hostinger

### Ya implementado:
✅ GZIP compression
✅ Browser caching (1 año para assets)
✅ Minificación recomendaciones en código
✅ Lazy loading de imágenes
✅ CDN para librerías externas
✅ Headers de seguridad
✅ Estructura SEO-friendly

### Por hacer (opcional):
- Minificar CSS/JS en producción
- Convertir imágenes a WebP
- Implementar Service Worker (PWA)
- Configurar Cloudflare
- Añadir subresource integrity (SRI)

## 🔐 Archivos Sensibles (No subir a Git)

Estos archivos NO deben estar en control de versiones:
```
.env
*.sql (backups)
*.log
vendor/ (si usas Composer)
node_modules/ (si usas npm)
```

Ver `.gitignore` para lista completa.

## 📞 Soporte

Para modificar archivos:
- **HTML:** Editar directamente con editor de texto
- **CSS:** Modificar variables en `:root` para cambios globales
- **JS:** Comentar/descomentar funciones según necesidad
- **PHP:** Seguir estructura existente

---

**Última actualización:** Enero 2026  
**Versión:** 1.0.0  
**Mantenido por:** Equipo FECASAM 2026
