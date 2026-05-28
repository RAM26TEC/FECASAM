# 📄 Conversión del Programa HTML a PDF

Se ha creado un documento de ejemplo en formato HTML que puedes convertir a PDF fácilmente.

## Archivo Disponible
- `programa-fecasam-2026-ejemplo.html` - Programa completo con diseño profesional

## 📋 Métodos para Convertir a PDF

### Método 1: Navegador (Más Fácil)

1. Abre el archivo `programa-fecasam-2026-ejemplo.html` en un navegador
2. Presiona `Ctrl + P` (Windows) o `Cmd + P` (Mac)
3. Selecciona "Guardar como PDF" o "Microsoft Print to PDF"
4. Ajusta configuración:
   - Márgenes: Predeterminados
   - Escala: 100%
   - Opciones: Gráficos de fondo activados
5. Guardar como: `programa-fecasam-2026.pdf`

**Recomendado:** Google Chrome o Microsoft Edge dan mejores resultados

### Método 2: Herramientas Online (Rápido)

**Sitios recomendados:**
- [HTML2PDF](https://html2pdf.com/)
- [PDFCrowd](https://pdfcrowd.com/)
- [CloudConvert](https://cloudconvert.com/html-to-pdf)

**Pasos:**
1. Subir el archivo HTML
2. Convertir
3. Descargar el PDF

### Método 3: Software Profesional

**Adobe Acrobat DC:**
1. Archivo → Crear → PDF desde archivo HTML
2. Seleccionar el archivo HTML
3. Guardar

**Microsoft Word:**
1. Abrir el HTML en Word
2. Archivo → Guardar como → PDF

### Método 4: PowerShell (Avanzado)

```powershell
# Usar wkhtmltopdf (necesita instalación)
wkhtmltopdf programa-fecasam-2026-ejemplo.html programa-fecasam-2026.pdf
```

## ✅ Verificación del PDF

Después de convertir, verifica que:
- [ ] El logo vea correctamente
- [ ] Los colores se mantienen (#8B5E3C, #D4A574)
- [ ] Las tablas están completas
- [ ] La paginación es correcta
- [ ] El texto es seleccionable
- [ ] El tamaño de archivo es razonable (< 1 MB sin imágenes)

## 🎨 Personalización

Si necesitas modificar el contenido:

1. Abre `programa-fecasam-2026-ejemplo.html` en un editor de texto
2. Busca las secciones que quieres cambiar
3. Modifica el contenido HTML
4. Guarda y vuelve a convertir a PDF

**Secciones principales:**
- `.header` - Encabezado con título y fechas
- `.day` - Programación por día
- `table` - Categorías de concurso
- `.info-box` - Cuadros de información

## 📤 Uso en el Sitio Web

Una vez convertido a PDF:

```bash
# Renombrar el archivo
mv programa-fecasam-2026.pdf assets/downloads/programa-fecasam-2026.pdf
```

El botón de descarga en el sitio web automáticamente lo enlazará.

## 💡 Tips Profesionales

1. **Optimizar tamaño:**
   - Usar herramientas como [Smallpdf](https://smallpdf.com/compress-pdf)
   - Reducir calidad de imágenes si incluyes fotos

2. **Añadir marca de agua:**
   - Usar Adobe Acrobat
   - O herramientas online como [PDF24](https://tools.pdf24.org/)

3. **Proteger el PDF:**
   - Puedes añadir contraseña o restricciones
   - Útil si el documento es preliminar

## 📞 Soporte

Si tienes problemas con la conversión, revisa:
- Que el navegador soporte impresión a PDF
- Que los estilos CSS se estén cargando
- Que el archivo HTML esté completo

---

**Nota:** Este es un documento de **ejemplo**. Asegúrate de actualizar las fechas, horarios y detalles según la información oficial del evento.
