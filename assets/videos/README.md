# 🎥 Videos Requeridos para FECASAM 2026

Esta carpeta debe contener los videos utilizados en el sitio web.

## 📹 Video Principal

### **hero-alpacas.mp4**

**Uso:** Video de fondo en la sección hero (primera pantalla)

**Especificaciones Técnicas:**
- **Formato:** MP4 (H.264 codec)
- **Resolución:** 1920x1080 pixels (Full HD) o 1280x720 (HD)
- **Duración:** 10-20 segundos (loop)
- **Peso máximo:** 5MB (importante para carga rápida)
- **FPS:** 30 fps
- **Audio:** Sin audio (muted)
- **Bitrate:** 1-2 Mbps

**Contenido Sugerido:**
- Alpacas pastando en el altiplano
- Paisajes de Macusani/Carabaya
- Escenas del evento en ediciones anteriores
- Artesanos trabajando fibra de alpaca
- Concursos de alpacas

**Características del Video:**
- Movimiento suave (evitar movimientos bruscos)
- Buena iluminación (paisajes diurnos)
- Colores vibrantes pero naturales
- Sin texto o watermarks
- Loop seamless (el inicio y fin se conectan bien)

## 🎬 Preparación del Video

### Paso 1: Grabar o Obtener Video
- Grabar con cámara estabilizada o usando trípode
- Aprovechar la luz natural (horas doradas: mañana o atardecer)
- Capturar escenas representativas del evento

### Paso 2: Editar
1. Recortar a 10-20 segundos
2. Estabilizar si tiene movimiento de cámara
3. Ajustar brillo/contraste/saturación
4. Agregar transición suave entre inicio y fin (para loop)
5. Exportar sin audio

### Paso 3: Optimizar para Web
```bash
# Usando FFmpeg para optimizar
ffmpeg -i input.mp4 -vcodec h264 -acodec none -crf 23 -preset slow -vf "scale=1920:1080" hero-alpacas.mp4

# Para reducir más el tamaño (720p)
ffmpeg -i input.mp4 -vcodec h264 -acodec none -crf 24 -preset slow -vf "scale=1280:720" hero-alpacas.mp4
```

## 🛠️ Herramientas Recomendadas

**Editores de Video:**
- [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/) - Gratis y profesional
- [OpenShot](https://www.openshot.org/) - Editor simple y gratuito
- [Adobe Premiere Pro](https://www.adobe.com/products/premiere.html) - Profesional (pago)
- [Shotcut](https://shotcut.org/) - Gratuito y multiplataforma

**Optimizadores:**
- [HandBrake](https://handbrake.fr/) - Compresor de video gratuito
- [CloudConvert](https://cloudconvert.com/) - Conversor online
- [FFmpeg](https://ffmpeg.org/) - Herramienta de línea de comandos

**Bancos de Videos Gratuitos:**
- [Pexels Videos](https://www.pexels.com/videos/)
- [Pixabay Videos](https://pixabay.com/videos/)
- [Mixkit](https://mixkit.co/)
- [Coverr](https://coverr.co/)

## 📊 Consideraciones de Rendimiento

### Tamaños de Archivo Recomendados:
- **Ideal:** 2-3 MB (carga rápida)
- **Aceptable:** 3-5 MB
- **Evitar:** Más de 5 MB (lentitud en móviles)

### Opciones según Conexión:
1. **Conexión rápida:** 1920x1080, 2-3 Mbps
2. **Conexión media:** 1280x720, 1-2 Mbps
3. **Móvil:** Considerar desactivar video automáticamente

## 🎨 Alternativas al Video

Si no se cuenta con video de calidad:

### Opción 1: Imagen Estática
- Usar hero-poster.jpg de alta calidad
- Aplicar efecto parallax con JavaScript
- Agregar overlay con animaciones CSS

### Opción 2: Slideshow de Imágenes
- Crear presentación de 3-5 imágenes
- Transiciones suaves cada 5 segundos
- Menos peso que video

### Opción 3: Video de Stock
- Buscar en bancos de videos gratuitos
- Palabras clave: "alpaca", "llama", "Andes", "Peru mountains"
- Verificar licencia de uso comercial

## 📋 Checklist

Antes de usar el video en producción:

- [ ] El video está en formato MP4 (H.264)
- [ ] La duración es menor a 20 segundos
- [ ] El peso es menor a 5 MB
- [ ] No tiene audio
- [ ] La resolución es adecuada (1080p o 720p)
- [ ] El loop es seamless (se repite bien)
- [ ] Se ve bien en móviles
- [ ] Carga rápidamente
- [ ] El contenido es apropiado y relevante
- [ ] No infringe derechos de autor

## 🚀 Implementación en el Sitio

El video se utiliza en `index.html`:

```html
<video class="hero-video" autoplay muted loop playsinline>
    <source src="assets/videos/hero-alpacas.mp4" type="video/mp4">
</video>
```

**Atributos importantes:**
- `autoplay` - Inicia automáticamente
- `muted` - Sin audio (necesario para autoplay)
- `loop` - Se repite infinitamente
- `playsinline` - Reproduce inline en iOS

## 💡 Tips Profesionales

1. **Grabación:**
   - Usa estabilizador o gimbal
   - Graba en RAW si es posible
   - Captura 30 segundos para tener opciones de edición

2. **Edición:**
   - Color grading sutil (tonos cálidos para reflejar la región)
   - Transición de 1-2 segundos al inicio (fade in)
   - Matching del primer y último frame para loop perfecto

3. **Optimización:**
   - H.264 es el codec más compatible
   - CRF entre 23-24 equilibra calidad/tamaño
   - Eliminar audio reduce 30-40% el tamaño

4. **Testing:**
   - Probar en Chrome, Firefox, Safari
   - Verificar en móviles (iOS y Android)
   - Comprobar carga con red lenta (3G)

## 📞 Notas

- El video es **opcional** - el sitio funciona sin él
- Si no se incluye video, se mostrará solo el overlay y el contenido
- Considerar crear versión mobile más ligera
- El video NO debe distraer del contenido principal

**Última actualización:** 27 de mayo de 2026
