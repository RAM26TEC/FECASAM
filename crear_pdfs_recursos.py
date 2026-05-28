#!/usr/bin/env python3
"""
Script para crear PDFs de recursos de ejemplo para FECASAM 2026
"""

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    import os
except ImportError:
    print("❌ Error: reportlab no está instalado.")
    print("Instalando reportlab...")
    import subprocess
    subprocess.run(["pip", "install", "reportlab"], check=True)
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    import os

def crear_pdf_recurso(filename, titulo, descripcion):
    """Crea un PDF de ejemplo con el título y descripción dados"""
    
    # Colores de FECASAM
    color_primario = HexColor("#6B4423")
    color_secundario = HexColor("#B8956A")
    color_acento = HexColor("#E67E22")
    
    # Crear canvas
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # Fondo beige claro
    c.setFillColor(HexColor("#F5E6D3"))
    c.rect(0, 0, width, height, fill=True, stroke=False)
    
    # Banner superior café
    c.setFillColor(color_primario)
    c.rect(0, height - 120, width, 120, fill=True, stroke=False)
    
    # Título del documento
    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width/2, height - 60, "FECASAM 2026")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height - 85, "XXXI Edición")
    
    # Subtítulo
    c.setFillColor(color_secundario)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(width/2, height - 105, "Capital Alpaquera del Mundo - Macusani, Puno")
    
    # Título del recurso
    c.setFillColor(color_primario)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - 170, titulo)
    
    # Línea decorativa
    c.setStrokeColor(color_acento)
    c.setLineWidth(2)
    c.line(100, height - 185, width - 100, height - 185)
    
    # Descripción
    c.setFillColor(color_primario)
    c.setFont("Helvetica", 12)
    
    # Dividir descripción en líneas
    y_position = height - 220
    for line in descripcion:
        c.drawCentredString(width/2, y_position, line)
        y_position -= 25
    
    # Contenido de ejemplo
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor("#333333"))
    
    content_y = height - 300
    c.drawString(60, content_y, "Este es un documento de ejemplo para FECASAM 2026.")
    content_y -= 20
    c.drawString(60, content_y, "El contenido final será proporcionado por la organización del evento.")
    content_y -= 40
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, content_y, "Información de Contacto:")
    content_y -= 25
    
    c.setFont("Helvetica", 10)
    c.drawString(80, content_y, "• Campo Ferial Julio E. Barreda - Macusani, Puno")
    content_y -= 18
    c.drawString(80, content_y, "• Fechas: 22 - 30 de Agosto de 2026")
    content_y -= 18
    c.drawString(80, content_y, "• Web: www.fecasam.gob.pe")
    content_y -= 18
    c.drawString(80, content_y, "• Email: info@fecasam.gob.pe")
    
    # Footer
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(HexColor("#999999"))
    c.drawCentredString(width/2, 50, "Feria Exposición de Camélidos Sudamericanos, Agropecuarios y Artesanales")
    c.drawCentredString(width/2, 35, "© 2026 FECASAM - Todos los derechos reservados")
    
    # Guardar PDF
    c.save()
    print(f"✓ PDF creado: {filename}")

def main():
    # Crear directorio si no existe
    output_dir = "assets/downloads"
    os.makedirs(output_dir, exist_ok=True)
    
    print("🎨 Creando PDFs de recursos para FECASAM 2026...\n")
    
    # Definir recursos
    recursos = [
        {
            "filename": "programa-fecasam-2026.pdf",
            "titulo": "Programa Oficial",
            "descripcion": [
                "Cronograma detallado de todas las actividades",
                "22 - 30 de Agosto de 2026",
                "Campo Ferial Julio E. Barreda, Macusani"
            ]
        },
        {
            "filename": "bases-concurso.pdf",
            "titulo": "Bases del Concurso",
            "descripcion": [
                "Reglamento completo para participantes",
                "Categorías y criterios de evaluación",
                "Premios y reconocimientos"
            ]
        },
        {
            "filename": "ruta-paqochanan.pdf",
            "titulo": "Ruta Paqochañan",
            "descripcion": [
                "Guía turística de acceso y atractivos",
                "Rutas desde principales ciudades",
                "Lugares de interés en Macusani"
            ]
        },
        {
            "filename": "catalogo-expositores.pdf",
            "titulo": "Catálogo de Expositores",
            "descripcion": [
                "Listado de stands y empresas participantes",
                "Directorio de contactos",
                "Plano del campo ferial"
            ]
        },
        {
            "filename": "manual-biotecnologia.pdf",
            "titulo": "Manual de Biotecnología",
            "descripcion": [
                "Técnicas de mejoramiento genético aplicado",
                "Innovaciones en crianza de camélidos",
                "Buenas prácticas ganaderas"
            ]
        }
    ]
    
    # Crear cada PDF
    for recurso in recursos:
        filepath = os.path.join(output_dir, recurso["filename"])
        crear_pdf_recurso(filepath, recurso["titulo"], recurso["descripcion"])
    
    print(f"\n✅ Se crearon {len(recursos)} archivos PDF en {output_dir}/")
    print("\n📄 Archivos creados:")
    for recurso in recursos:
        print(f"   - {recurso['filename']}")

if __name__ == "__main__":
    main()
