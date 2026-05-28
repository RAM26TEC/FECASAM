# ⚠️ IMPORTANTE: Optimización del Video

El video `hero-alpacas.mp4` actualmente pesa **308 MB**, lo cual es **demasiado grande** para un sitio web.

## 🚨 Problema Actual

- **Tamaño actual:** 308 MB
- **Tamaño recomendado:** 3-5 MB (máximo)
- **Impacto:** 
  - Carga MUY lenta del sitio
  - Consumo excesivo de datos móviles
  - Mala experiencia de usuario

## ✅ Solución: Optimizar el Video

### Método 1: FFmpeg (Recomendado)

Si tienes FFmpeg instalado:

```powershell
cd "d:\2026\SISTEMAS\FECASAM 2026\assets\videos"

# Opción 1: Calidad media (2-3 MB)
ffmpeg -i hero-alpacas.mp4 -vcodec h264 -crf 28 -preset slow -vf "scale=1280:720" -t 15 -an hero-alpacas-optimized.mp4

# Opción 2: Calidad alta (4-5 MB)
ffmpeg -i hero-alpacas.mp4 -vcodec h264 -crf 24 -preset slow -vf "scale=1920:1080" -t 15 -an hero-alpacas-optimized.mp4

# Después, reemplazar el original
mv hero-alpacas-optimized.mp4 hero-alpacas.mp4
```

**Parámetros explicados:**
- `-crf 24-28` = Calidad (menor número = mejor calidad, mayor tamaño)
- `-vf "scale=1280:720"` = Reducir resolución a HD
- `-t 15` = Cortar a 15 segundos (suficiente para loop)
- `-an` = Remover audio (no necesario)

### Método 2: HandBrake (Interfaz Gráfica)

1. Descargar [HandBrake](https://handbrake.fr/)
2. Abrir el video
3. Configuración:
   - **Preset:** Web → Gmail Large 3 Minutes 720p30
   - **Dimensions:** 1280x720 o 1920x1080
   - **Framerate:** 30 FPS
   - **Video Codec:** H.264
   - **Quality:** RF 24-28
4. Recortar a 15-20 segundos
5. Guardar

### Método 3: Online (Fácil pero menos control)

**Sitios recomendados:**
- [Clipchamp](https://clipchamp.com/) - Editor online
- [CloudConvert](https://cloudconvert.com/mp4-compress) - Compresor
- [FreeConvert](https://www.freeconvert.com/video-compressor) - Gratis

**Pasos:**
1. Subir video
2. Seleccionar calidad "Medium" o "Web"
3. Recortar a 10-15 segundos
4. Descargar comprimido

## 📊 Tamaños Objetivo

| Resolución | Calidad | Duración | Tamaño Esperado |
|------------|---------|----------|-----------------|
| 1280x720   | Media   | 15 seg   | 2-3 MB          |
| 1920x1080  | Media   | 15 seg   | 4-5 MB          |
| 1280x720   | Alta    | 20 seg   | 5-7 MB          |

## 🎬 Tips Adicionales

1. **Recortar el video:**
   - Solo necesitas 10-15 segundos para el loop del hero
   - Selecciona la mejor toma (movimiento suave, buena iluminación)

2. **Resolución:**
   - Para hero web, 720p (1280x720) es suficiente
   - Nadie notará la diferencia en pantallas normales

3. **Framerate:**
   - 30 FPS es perfecto para web
   - No necesitas 60 FPS

4. **Audio:**
   - El video hero es muted, así que eliminar audio reduce peso

## 🚀 Alternativa: Usar Imagen Estática

Si no puedes optimizar el video, considera:

1. **Extraer un frame del video:**
```powershell
ffmpeg -i hero-alpacas.mp4 -ss 00:00:03 -vframes 1 hero-poster.jpg
```

2. **Usar la imagen como fondo** y desactivar video en móviles

En `main.js` ya existe código que pausa el video en móviles:
```javascript
// Pause video on mobile to save bandwidth
if (isMobileDevice()) {
    DOM.heroVideo.pause();
    DOM.heroVideo.poster = 'assets/images/hero-poster.jpg';
}
```

## ✅ Verificación

Después de optimizar:

```powershell
# Verificar tamaño
Get-ChildItem "hero-alpacas.mp4" | Select-Object Name, Length

# Si es mayor a 10 MB, optimizar más
```

## 📞 ¿Necesitas Ayuda?

Si no tienes las herramientas o experiencia:

1. Contacta a un editor de video
2. Usa servicios online (Fiverr, Upwork)
3. O simplemente usa imagen estática en lugar de video

---

**Prioridad:** 🔴 **ALTA** - El sitio no debería lanzarse con un video de 308 MB

**Tiempo estimado:** 30-60 minutos (con herramientas correctas)
