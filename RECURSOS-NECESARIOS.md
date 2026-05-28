# 📦 CHECKLIST DE RECURSOS NECESARIOS

Antes de subir el sitio a producción, asegúrate de tener todos estos recursos:

## 🖼️ Imágenes Requeridas

### Logos
- [ ] `assets/images/logo.png` - Logo principal (fondo oscuro)
- [ ] `assets/images/logo-light.png` - Logo claro (fondo claro)
- [ ] `assets/images/favicon.png` - Favicon (32x32px o 64x64px)

### Open Graph / SEO
- [ ] `assets/images/og-image.jpg` - Imagen para compartir en redes (1200x630px)

### Sección About/Features
- [ ] `assets/images/fibra-alpaca.jpg` - Imagen de fibra de alpaca
- [ ] `assets/images/carne-camelidos.jpg` - Imagen de carne de camélidos

### Hero Section (Opcional)
- [ ] `assets/images/hero-background.jpg` - Imagen de fondo alternativa

## 🎥 Videos

### Hero Video
- [ ] `assets/videos/hero-alpacas.mp4` - Video de alpacas/glaciares (15-30 segundos)
  - Formato: MP4 (H.264)
  - Resolución: 1920x1080 o superior
  - Tamaño: <10MB (optimizado)
  - Mudo (sin audio)

**Alternativa gratuita:** Usa videos de [Pexels](https://www.pexels.com/search/videos/alpaca/) o [Pixabay](https://pixabay.com/videos/search/alpaca/)

## 📄 PDFs Descargables

- [ ] `assets/downloads/programa-fecasam-2026.pdf` - Programa oficial
- [ ] `assets/downloads/bases-concurso.pdf` - Bases del concurso
- [ ] `assets/downloads/ruta-paqochanan.pdf` - Guía de acceso
- [ ] `assets/downloads/catalogo-expositores.pdf` - Catálogo de expositores
- [ ] `assets/downloads/manual-biotecnologia.pdf` - Manual técnico

## 🎨 Especificaciones de Diseño

### Logos
```
Logo principal:
- Formato: PNG con transparencia
- Dimensiones: 300x100px (aproximado)
- Peso: <50KB

Favicon:
- Formato: PNG o ICO
- Dimensiones: 32x32px o 64x64px
- Peso: <10KB
```

### Imágenes de Contenido
```
Imágenes de features:
- Formato: JPG (optimizado) o WebP
- Dimensiones: 800x600px
- Peso: <200KB cada una
- Calidad: 80-85%

Open Graph Image:
- Formato: JPG
- Dimensiones: 1200x630px
- Peso: <300KB
```

### Videos
```
Hero Video:
- Codec: H.264
- Contenedor: MP4
- Resolución: 1920x1080
- Duración: 15-30 segundos
- Sin audio
- Loop: Sí
- Peso: <10MB
```

## 🔧 Herramientas Recomendadas

### Para Imágenes

**Optimización:**
- [TinyPNG](https://tinypng.com/) - Compresión de PNG/JPG
- [Squoosh](https://squoosh.app/) - Editor y compresor online
- [SVGOMG](https://jakearchibald.github.io/svgomg/) - Para SVG

**Edición:**
- [Photopea](https://www.photopea.com/) - Editor online gratuito
- GIMP - Software gratuito de escritorio
- Canva - Para diseños rápidos

### Para Videos

**Edición y Compresión:**
- [HandBrake](https://handbrake.fr/) - Compresor de video gratuito
- [CloudConvert](https://cloudconvert.com/mp4-converter) - Conversor online
- FFmpeg - Herramienta de línea de comandos

**Ejemplo FFmpeg para optimizar:**
```bash
ffmpeg -i input.mp4 -vcodec h264 -acodec none -vf scale=1920:1080 -b:v 2M output.mp4
```

### Para PDFs

**Creación:**
- LibreOffice Writer + Exportar a PDF
- Google Docs + Descargar como PDF
- Adobe Acrobat (de pago)

**Optimización:**
- [PDF Compressor](https://www.ilovepdf.com/compress_pdf)
- Adobe Acrobat Pro
- Ghostscript

## 📝 Plantillas de Contenido

### Programa Oficial
```
Contenido sugerido:
1. Introducción al evento
2. Cronograma día por día
3. Descripción de actividades
4. Mapa del campo ferial
5. Información de contacto
```

### Bases del Concurso
```
Contenido sugerido:
1. Objetivos del concurso
2. Categorías y subcategorías
3. Requisitos de participación
4. Criterios de evaluación
5. Premios y reconocimientos
6. Proceso de inscripción
7. Contacto e información
```

## 🎯 Prioridades

### Crítico (Necesario para producción)
1. Logo principal
2. Favicon
3. Al menos 1-2 imágenes de contenido
4. Programa oficial PDF

### Importante (Recomendado)
1. Video hero (puede usar imagen estática temporalmente)
2. Todos los PDFs
3. Open Graph image

### Opcional (Mejora la experiencia)
1. Logos alternativos
2. Imágenes adicionales
3. Material multimedia extra

## 🔄 Soluciones Temporales

### Si no tienes el video:
Puedes usar una imagen estática modificando en HTML:

```html
<!-- En lugar de video -->
<div class="hero-video-container">
    <img src="assets/images/hero-background.jpg" class="hero-video" alt="FECASAM 2026">
    <div class="hero-overlay"></div>
</div>
```

### Si no tienes los PDFs:
Simplemente oculta la sección de recursos temporalmente agregando en CSS:

```css
.resources-section {
    display: none;
}
```

O comenta la sección en el HTML.

### Si no tienes imágenes específicas:
Usa placeholders de:
- [Unsplash](https://unsplash.com/) - Fotos gratuitas
- [Pexels](https://www.pexels.com/) - Fotos y videos
- [Pixabay](https://pixabay.com/) - Multimedia libre

## ✅ Checklist Final

Marca cuando tengas cada recurso:

**Logos:**
- [ ] Logo principal
- [ ] Logo light
- [ ] Favicon

**Imágenes:**
- [ ] OG image
- [ ] Fibra alpaca
- [ ] Carne camélidos
- [ ] Hero background (opcional)

**Videos:**
- [ ] Hero video

**PDFs:**
- [ ] Programa
- [ ] Bases
- [ ] Ruta Paqochañan
- [ ] Catálogo
- [ ] Manual

---

**Nota:** Todos los recursos deben estar optimizados para web antes de subirlos al servidor.
