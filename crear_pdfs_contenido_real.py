#!/usr/bin/env python3
"""
Script para crear PDFs de recursos con contenido real para FECASAM 2026
Basado en el documento oficial del evento
"""

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm, mm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Frame
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.platypus.flowables import Flowable
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    import os
except ImportError:
    print("❌ Error: reportlab no está instalado.")
    print("Instalando reportlab...")
    import subprocess
    subprocess.run(["pip", "install", "reportlab"], check=True)
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm, mm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.platypus.flowables import Flowable
    import os

# Colores de FECASAM (paleta mejorada)
COLOR_PRIMARIO = HexColor("#6B4423")
COLOR_SECUNDARIO = HexColor("#B8956A")
COLOR_ACENTO = HexColor("#E67E22")
COLOR_OSCURO = HexColor("#4A2F1A")
COLOR_CLARO = HexColor("#F5E6D3")
COLOR_BLANCO = white
COLOR_GRIS_CLARO = HexColor("#F8F8F8")
COLOR_GRIS_MEDIO = HexColor("#CCCCCC")

# Clase para crear cajas decorativas
class ColorBox(Flowable):
    """Caja de color decorativa para destacar contenido"""
    def __init__(self, width, height, color):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)

# Clase para líneas decorativas
class DecorativeLine(Flowable):
    """Línea decorativa horizontal"""
    def __init__(self, width, color, thickness=2):
        Flowable.__init__(self)
        self.width = width
        self.height = thickness
        self.color = color
        self.thickness = thickness
    
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)

def crear_estilos():
    """Crea estilos personalizados y modernos para los documentos"""
    styles = getSampleStyleSheet()
    
    # Estilo para título principal - más grande y bold
    styles.add(ParagraphStyle(
        name='TituloPrincipal',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=COLOR_PRIMARIO,
        spaceAfter=8,
        spaceBefore=10,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=32
    ))
    
    # Estilo para subtítulo elegante
    styles.add(ParagraphStyle(
        name='Subtitulo',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=COLOR_SECUNDARIO,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    ))
    
    # Estilo para fecha/ubicación
    styles.add(ParagraphStyle(
        name='InfoEvento',
        parent=styles['Normal'],
        fontSize=11,
        textColor=COLOR_ACENTO,
        spaceAfter=5,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    
    # Estilo para sección con fondo
    styles.add(ParagraphStyle(
        name='Seccion',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=COLOR_BLANCO,
        spaceAfter=12,
        spaceBefore=18,
        fontName='Helvetica-Bold',
        backColor=COLOR_PRIMARIO,
        leftIndent=10,
        rightIndent=10,
        leading=20
    ))
    
    # Estilo para subsección moderna
    styles.add(ParagraphStyle(
        name='Subseccion',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=COLOR_PRIMARIO,
        spaceAfter=8,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        borderColor=COLOR_SECUNDARIO,
        borderWidth=0,
        borderPadding=5,
        leftIndent=5
    ))
    
    # Estilo para cuerpo de texto limpio
    styles.add(ParagraphStyle(
        name='CuerpoTexto',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=HexColor("#333333"),
        spaceAfter=6,
        alignment=TA_LEFT,
        fontName='Helvetica',
        leading=14
    ))
    
    # Estilo para texto destacado
    styles.add(ParagraphStyle(
        name='Destacado',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=COLOR_OSCURO,
        spaceAfter=10,
        spaceBefore=5,
        fontName='Helvetica-Bold',
        backColor=COLOR_CLARO,
        leftIndent=15,
        rightIndent=15,
        borderPadding=8
    ))
    
    # Estilo para lista con iconos
    styles.add(ParagraphStyle(
        name='ListaItem',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=HexColor("#333333"),
        spaceAfter=4,
        leftIndent=15,
        bulletIndent=5,
        fontName='Helvetica',
        leading=13
    ))
    
    # Estilo para caja de info
    styles.add(ParagraphStyle(
        name='CajaInfo',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=COLOR_OSCURO,
        spaceAfter=10,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        backColor=COLOR_CLARO,
        borderColor=COLOR_ACENTO,
        borderWidth=2,
        borderPadding=10
    ))
    
    return styles

def agregar_header(elementos, styles):
    """Agrega un encabezado moderno y atractivo"""
    # Línea decorativa superior
    elementos.append(DecorativeLine(17*cm, COLOR_ACENTO, 3))
    elementos.append(Spacer(1, 5*mm))
    
    # Título principal con estilo
    elementos.append(Paragraph("✦ FECASAM 2026 ✦", styles['TituloPrincipal']))
    elementos.append(Paragraph("XXXI Feria de Camélidos Sudamericanos", styles['Subtitulo']))
    
    # Información clave con iconos
    elementos.append(Spacer(1, 3*mm))
    elementos.append(Paragraph("📍 Macusani, Carabaya, Puno, Perú", styles['InfoEvento']))
    elementos.append(Paragraph("📅 22 - 30 de Agosto, 2026", styles['InfoEvento']))
    
    # Línea decorativa inferior
    elementos.append(Spacer(1, 5*mm))
    elementos.append(DecorativeLine(17*cm, COLOR_ACENTO, 3))
    elementos.append(Spacer(1, 8*mm))

def crear_programa_pdf(filename, styles):
    """Crea el PDF del programa oficial con diseño moderno"""
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm, 
                          leftMargin=20*mm, rightMargin=20*mm)
    elementos = []
    
    agregar_header(elementos, styles)
    
    # Título del documento
    elementos.append(Paragraph("📋 PROGRAMA OFICIAL", styles['TituloPrincipal']))
    elementos.append(Spacer(1, 5*mm))
    
    # Caja de información destacada
    elementos.append(Paragraph(
        "📍 Campo Ferial Julio E. Barreda Aragón, Macusani<br/>"
        "🗓️ 22-30 Agosto 2026 | 📧 fecasam2026@gmail.com | 📞 979 007 682",
        styles['CajaInfo']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Cronograma compacto y visual
    elementos.append(Paragraph("📅 CRONOGRAMA", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    cronograma = [
        ["FECHA", "ACTIVIDAD PRINCIPAL", "HORA"],
        ["22-23 AGO", "Registro de animales", "8:00 - 16:00"],
        ["24-25 AGO", "Admisión oficial de ganado", "Todo el día"],
        ["25 AGO", "🎉 Inauguración + Llamas Sak'atis", "11:00 AM"],
        ["26-27 AGO", "🏆 Juzgamiento Alpacas y Llamas", "9:00 - 18:00"],
        ["26 AGO", "🍴 Concurso Gastronomía", "Todo el día"],
        ["26 AGO", "🎨 Concurso Artesanía", "Todo el día"],
        ["27 AGO", "✂️ Esquila y Mejor Vellón", "13:00 PM"],
        ["28 AGO", "💼 Rueda Negocios + Desfile Moda", "Todo el día"],
        ["29 AGO", "🎓 Congreso Académico", "Todo el día"],
        ["30 AGO", "🎊 Clausura y Premiación", "16:00 PM"]
    ]
    
    tabla = Table(cronograma, colWidths=[25*mm, 95*mm, 30*mm])
    tabla.setStyle(TableStyle([
        # Encabezado
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_ACENTO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        # Filas alternas
        ('BACKGROUND', (0, 1), (-1, -1), COLOR_CLARO),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'CENTER'),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        # Bordes
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
        ('BOX', (0, 0), (-1, -1), 1.5, COLOR_PRIMARIO),
    ]))
    elementos.append(tabla)
    elementos.append(Spacer(1, 7*mm))
    
    # Componentes del evento - diseño compacto con iconos
    elementos.append(Paragraph("🎯 COMPONENTES PRINCIPALES", styles['Seccion']))
    elementos.append(Spacer(1, 4*mm))
    
    componentes_data = [
        ["🏆", "Concurso Alpacas/Llamas", "Juzgamiento razas Huacaya, Suri, Ccara, Ch'aku"],
        ["👗", "Desfile de Moda", "Colecciones exclusivas con fibra de alpaca"],
        ["🍽️", "Gastronomía", "Platos gourmet a base de carne de camélidos"],
        ["💼", "Rueda de Negocios", "Acuerdos comerciales y exportación"],
        ["🎓", "Congresos", "Mejoramiento genético y sostenibilidad"],
        ["🗺️", "Ruta Paqocha", "Tours y sitios arqueológicos de Macusani"]
    ]
    
    tabla_comp = Table(componentes_data, colWidths=[10*mm, 50*mm, 90*mm])
    tabla_comp.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (1, 0), (1, -1), COLOR_PRIMARIO),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [COLOR_GRIS_CLARO, COLOR_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
    ]))
    elementos.append(tabla_comp)
    elementos.append(Spacer(1, 7*mm))
    
    # Caja de contacto final
    elementos.append(DecorativeLine(17*cm, COLOR_SECUNDARIO, 1))
    elementos.append(Spacer(1, 3*mm))
    elementos.append(Paragraph(
        "<b>Organiza:</b> Municipalidad Provincial de Carabaya · PromPerú · Comité FECASAM 2026",
        styles['CuerpoTexto']
    ))
    
    doc.build(elementos)
    print(f"✓ PDF creado: {filename}")

def crear_bases_concurso_pdf(filename, styles):
    """Crea el PDF de bases del concurso con diseño moderno"""
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm,
                          leftMargin=20*mm, rightMargin=20*mm)
    elementos = []
    
    agregar_header(elementos, styles)
    
    # Título del documento
    elementos.append(Paragraph("🏆 BASES DEL CONCURSO", styles['TituloPrincipal']))
    elementos.append(Spacer(1, 5*mm))
    
    # Caja de objetivo destacado
    elementos.append(Paragraph(
        "🎯 Promover la alpaca y llama, revalorar la cadena textil y fomentar la competitividad en conjunto con Perú Moda Deco.",
        styles['CajaInfo']
    ))
    elementos.append(Spacer(1, 6*mm))
    
    # Participantes
    elementos.append(Paragraph("👥 PARTICIPANTES", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "✓ Productores individuales de alpacas/llamas · ✓ Empresas y grupos organizados · "
        "✓ Productores agropecuarios y artesanales · ✓ Entidades públicas y privadas",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 5*mm))
    
    # Inscripciones destacadas
    elementos.append(Paragraph("📝 INSCRIPCIONES", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    
    insc_data = [
        ["📅 Fecha límite", "15 de Junio, 2026"],
        ["💰 Costo", "S/. 5.00 por animal"],
        ["🦙 Mínimo", "10 animales por expositor"],
        ["📍 Lugar", "Oficina Desarrollo Económico Local - Carabaya"]
    ]
    
    tabla_insc = Table(insc_data, colWidths=[45*mm, 105*mm])
    tabla_insc.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9.5),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (0, -1), COLOR_PRIMARIO),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [COLOR_GRIS_CLARO, COLOR_CLARO]),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
    ]))
    elementos.append(tabla_insc)
    elementos.append(Spacer(1, 6*mm))
    
    # Categorías compactas
    elementos.append(Paragraph("📊 CATEGORÍAS", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    
    cat_data = [
        ["CAT", "DESCRIPCIÓN", "EDAD"],
        ["A1", "Tui menor (dientes de leche)", "< 1 año"],
        ["A2", "Tui mayor (dientes de leche)", "1-2 años"],
        ["B", "Jóvenes con 2 dientes", "> 2 años"],
        ["C", "Con 4 dientes", "> 3 años"],
        ["D", "Adultos, boca llena", "≥ 4 años"]
    ]
    
    tabla_cat = Table(cat_data, colWidths=[20*mm, 95*mm, 35*mm])
    tabla_cat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_ACENTO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'CENTER'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
        ('BOX', (0, 0), (-1, -1), 1, COLOR_PRIMARIO),
    ]))
    elementos.append(tabla_cat)
    elementos.append(Spacer(1, 6*mm))
    
    # Criterios de juzgamiento destacado
    elementos.append(Paragraph("⚖️ JUZGAMIENTO", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "70% CALIDAD DE FIBRA  |  30% CONFORMACIÓN FENOTÍPICA",
        styles['Destacado']
    ))
    elementos.append(Spacer(1, 4*mm))
    
    # Tabla de puntuación compacta
    puntos = [
        ["POSICIÓN", "PTS"], 
        ["🥇 Gran Campeón de la Raza", "10"],
        ["🥈 Reservado Gran Campeón", "8"],
        ["Campeón Mayor y Menor", "7"],
        ["Reservado Campeón", "6"],
        ["1° Lugar Categoría", "5"],
        ["2° Lugar Categoría", "4"],
        ["3° Lugar Categoría", "3"],
        ["4° Lugar Categoría", "2"],
        ["5° Lugar Categoría", "1"]
    ]
    
    tabla_puntos = Table(puntos, colWidths=[125*mm, 25*mm])
    tabla_puntos.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARIO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
    ]))
    elementos.append(tabla_puntos)
    elementos.append(Spacer(1, 6*mm))
    
    # No se admiten - compacto
    elementos.append(Paragraph("❌ NO SE ADMITEN", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "• Características no correspondientes a la raza<br/>"
        "• Lunares, manchas o defectos inadmisibles<br/>"
        "• Sin disposiciones sanitarias vigentes<br/>"
        "• Defectos congénitos o hereditarios<br/>"
        "• Parásitos externos (sarna, piojo, garrapata)<br/>"
        "• Ocultamiento de defectos con tintes<br/>"
        "• Fibra inadecuada (>12-15cm huacaya, >30-35cm suri)",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 6*mm))
    
    # Premios
    elementos.append(Paragraph("🎁 PREMIOS", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    
    premios = [
        ["LUGAR", "COLOR ESCARAPELA"],
        ["🥇 1° Lugar", "🔴 Rojo y Blanco"],
        ["🥈 2° Lugar", "🟢 Verde y Blanco"],
        ["🥉 3° Lugar", "🔵 Celeste y Blanco"],
        ["4° Lugar", "Azul"],
        ["5° Lugar", "Amarillo"],
        ["Mención Honrosa", "Morado"]
    ]
    
    tabla_premios = Table(premios, colWidths=[60*mm, 90*mm])
    tabla_premios.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_ACENTO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
        ('BOX', (0, 0), (-1, -1), 1, COLOR_PRIMARIO),
    ]))
    elementos.append(tabla_premios)
    elementos.append(Spacer(1, 5*mm))
    
    # Nota final
    elementos.append(Paragraph(
        "📌 Admisión: 24-25 agosto hasta 16:00 hrs | Bandas especiales para campeones con flecos dorados/plateados",
        styles['Destacado']
    ))
    
    doc.build(elementos)
    print(f"✓ PDF creado: {filename}")

def crear_ruta_paqochanan_pdf(filename, styles):
    """Crea el PDF de la Ruta Paqochañan con diseño moderno"""
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm,
                          leftMargin=20*mm, rightMargin=20*mm)
    elementos = []
    
    agregar_header(elementos, styles)
    
    # Título del documento
    elementos.append(Paragraph("🗺️ RUTA PAQOCHAÑAN", styles['TituloPrincipal']))
    elementos.append(Paragraph("Turismo Vivencial en la Capital Alpaquera del Mundo", styles['Subtitulo']))
    elementos.append(Spacer(1, 5*mm))
    
    # Caja destacada
    elementos.append(Paragraph(
        "🎯 Promover internacionalmente 'LA GRAN RUTA DE LA ALPACA' como destino de turismo vivencial y cultural único en el mundo.",
        styles['CajaInfo']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Atractivos principales - compacto y visual
    elementos.append(Paragraph("✨ ATRACTIVOS PRINCIPALES", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    atractivos = [
        ["🦙", "Capital Alpaquera", "Mejores centros de producción con alpacas de élite"],
        ["🏭", "Centros de Producción", "Visitas guiadas desde crías hasta esquila"],
        ["⛰️", "Cordillera Carabaya", "Apu Allinccapac + Glaciar Qelccaya (más grande del mundo)"],
        ["🎨", "Pinturas Rupestres", "Arte ancestral de camélidos sudamericanos"],
        ["🏛️", "Bosque Sintilla", "Formaciones rocosas estilo ciudad gótica"],
        ["🌴", "Ruta a la Selva", "Travesía por diversos pisos ecológicos"],
        ["🎭", "Festivales", "Música y danzas tradicionales de Carabaya"]
    ]
    
    tabla_atractivos = Table(atractivos, colWidths=[10*mm, 45*mm, 95*mm])
    tabla_atractivos.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (1, 0), (1, -1), COLOR_PRIMARIO),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
    ]))
    elementos.append(tabla_atractivos)
    elementos.append(Spacer(1, 7*mm))
    
    # Cómo llegar - compacto
    elementos.append(Paragraph("🚌 CÓMO LLEGAR", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    rutas_data = [
        ["DESDE", "TIEMPO", "DETALLES"],
        ["Juliaca", "6 horas", "Carretera asfaltada, buses diarios"],
        ["Puno", "7 horas", "Salidas matutinas recomendadas"],
        ["Cusco", "8 horas", "Ruta escénica vía Urcos-Ocongate"]
    ]
    
    tabla_rutas = Table(rutas_data, colWidths=[40*mm, 30*mm, 80*mm])
    tabla_rutas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_ACENTO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
        ('BOX', (0, 0), (-1, -1), 1, COLOR_PRIMARIO),
    ]))
    elementos.append(tabla_rutas)
    elementos.append(Spacer(1, 7*mm))
    
    # Recomendaciones compactas
    elementos.append(Paragraph("💡 RECOMENDACIONES", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "⛰️ <b>Altitud 4,315 msnm</b> · Aclimatarse en Puno/Juliaca<br/>"
        "🧥 <b>Clima frío</b> · Llevar ropa abrigadora, gorros, guantes<br/>"
        "📅 <b>Mejor época</b> · Mayo-Septiembre (seca) · Agosto ideal (FECASAM)<br/>"
        "🕶️ <b>Protección</b> · Bloqueador, lentes, sombrero, capas de ropa<br/>"
        "💊 <b>Salud</b> · Consultar por medicación anti-soroche<br/>"
        "📸 <b>Fotografía</b> · Mejores tomas al amanecer y atardecer",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Servicios disponibles
    elementos.append(Paragraph("🏨 SERVICIOS", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "✓ Alojamiento en hostales locales · ✓ Gastronomía típica · ✓ Guías certificados · "
        "✓ Transporte turístico · ✓ Artesanía de fibra de alpaca · ✓ Stand info en FECASAM",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Contacto final
    elementos.append(DecorativeLine(17*cm, COLOR_SECUNDARIO, 1))
    elementos.append(Spacer(1, 3*mm))
    elementos.append(Paragraph(
        "📧 fecasam2026@gmail.com | 📞 979 007 682 | 📍 Municipalidad de Carabaya",
        styles['CuerpoTexto']
    ))
    
    doc.build(elementos)
    print(f"✓ PDF creado: {filename}")

def crear_catalogo_expositores_pdf(filename, styles):
    """Crea el PDF del catálogo de expositores con diseño moderno"""
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm,
                          leftMargin=20*mm, rightMargin=20*mm)
    elementos = []
    
    agregar_header(elementos, styles)
    
    # Título del documento
    elementos.append(Paragraph("📋 GUÍA PARA EXPOSITORES", styles['TituloPrincipal']))
    elementos.append(Spacer(1, 5*mm))
    
    # Caja bienvenida
    elementos.append(Paragraph(
        "🎉 La feria más importante del mundo dedicada a camélidos sudamericanos. "
        "9 días de intercambio comercial, cultural y académico.",
        styles['CajaInfo']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Categorías de participación - compacto
    elementos.append(Paragraph("🎯 CATEGORÍAS", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    categorias_data = [
        ["CATEGORÍA", "DESCRIPCIÓN"],
        ["🦙 Camélidos", "Criadores individuales, asociaciones y empresas ganaderas"],
        ["🎨 Artesanos", "Textiles y artículos de fibra (manual o mecánica)"],
        ["🍴 Gastronomía", "Platos innovadores con carne de camélidos"],
        ["🛒 Comercio", "Insumos agropecuarios, herramientas y productos"],
        ["🏛️ Instituciones", "Capacitación, asesoría técnica y financiamiento"]
    ]
    
    tabla_cat = Table(categorias_data, colWidths=[40*mm, 110*mm])
    tabla_cat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_ACENTO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
        ('BOX', (0, 0), (-1, -1), 1, COLOR_PRIMARIO),
    ]))
    elementos.append(tabla_cat)
    elementos.append(Spacer(1, 7*mm))
    
    # Requisitos simplificados
    elementos.append(Paragraph("📝 REQUISITOS", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    elementos.append(Paragraph("<b>🦙 Camélidos:</b>", styles['Subseccion']))
    elementos.append(Paragraph(
        "✓ Inscripción hasta 15 junio · ✓ Mín. 10 animales · ✓ Constancia productor/RUC · "
        "✓ S/. 5.00 por animal · ✓ Certificados sanitarios",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 3*mm))
    
    elementos.append(Paragraph("<b>🎨 Artesanos y Comerciantes:</b>", styles['Subseccion']))
    elementos.append(Paragraph(
        "✓ Inscripción 1-31 julio · ✓ Muestras de productos · ✓ Stand propio o asignado · "
        "✓ Normas sanitarias · ✓ Respetar horarios",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Beneficios destacados
    elementos.append(Paragraph("🎁 BENEFICIOS", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "✨ Miles de visitantes internacionales durante 9 días<br/>"
        "🤝 Networking con compradores y exportadores globales<br/>"
        "💼 Rueda de negocios para contratos comerciales<br/>"
        "🏆 Premios y reconocimientos que aumentan valor<br/>"
        "🎓 Acceso a charlas, talleres y congresos<br/>"
        "📢 Difusión en medios nacionales e internacionales",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Servicios del campo ferial - tabla compacta
    elementos.append(Paragraph("🏕️ SERVICIOS EN CAMPO FERIAL", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    servicios = [
        ["SERVICIO", "DISPONIBILIDAD"],
        ["🏗️ Pabellones techados", "Espacios cubiertos para todos"],
        ["⚡ Energía eléctrica", "Conexiones en cada pabellón"],
        ["💧 Agua potable", "Suministro continuo"],
        ["🔒 Seguridad 24/7", "Vigilancia permanente"],
        ["🚻 SS.HH.", "Baños en todo el ferial"],
        ["🍽️ Comedor", "Alimentación para expositores"],
        ["🅿️ Estacionamiento", "Zona de parqueo"],
        ["🏥 Primeros auxilios", "Posta médica básica"]
    ]
    
    tabla_serv = Table(servicios, colWidths=[70*mm, 80*mm])
    tabla_serv.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARIO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
    ]))
    elementos.append(tabla_serv)
    elementos.append(Spacer(1, 7*mm))
    
    # Normas compactas
    elementos.append(Paragraph("⚖️ NORMAS DE CONDUCTA", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "✓ Mantener limpieza · ❌ Prohibido alcohol · ⏰ Respetar horarios · "
        "🤝 Trato respetuoso · ❌ No armas · 📋 Cumplir disposiciones del comisario",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Contacto final
    elementos.append(DecorativeLine(17*cm, COLOR_SECUNDARIO, 1))
    elementos.append(Spacer(1, 3*mm))
    elementos.append(Paragraph(
        "📍 <b>Inscripciones:</b> Oficina Desarrollo Económico Local - Municipalidad de Carabaya<br/>"
        "📧 fecasam2026@gmail.com | 📞 979 007 682 | ⏰ Lunes-Viernes 8:00-17:00",
        styles['CuerpoTexto']
    ))
    
    doc.build(elementos)
    print(f"✓ PDF creado: {filename}")

def crear_manual_biotecnologia_pdf(filename, styles):
    """Crea el PDF del manual de biotecnología con diseño moderno"""
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm,
                          leftMargin=20*mm, rightMargin=20*mm)
    elementos = []
    
    agregar_header(elementos, styles)
    
    # Título del documento
    elementos.append(Paragraph("🧬 BIOTECNOLOGÍA APLICADA", styles['TituloPrincipal']))
    elementos.append(Paragraph("Mejoramiento Genético de Camélidos", styles['Subtitulo']))
    elementos.append(Spacer(1, 5*mm))
    
    # Caja de visión
    elementos.append(Paragraph(
        "🎯 Posicionar la alpaca peruana y sus productos derivados con calidad y cantidad en el mercado mundial.",
        styles['CajaInfo']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Objetivos compactos
    elementos.append(Paragraph("🎯 OBJETIVOS DEL MEJORAMIENTO", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "🧵 <b>Calidad fibra:</b> Finura, densidad, longitud<br/>"
        "📈 <b>Productividad:</b> Peso de vellón<br/>"
        "🦙 <b>Conformación:</b> Estándares raciales<br/>"
        "🛡️ <b>Adaptabilidad:</b> Resistencia a enfermedades<br/>"
        "👶 <b>Reproducción:</b> Fertilidad y sobrevivencia<br/>"
        "📊 <b>Homogeneidad:</b> Estandarización del rebaño",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 6*mm))
    
    # Técnicas de selección - tabla
    elementos.append(Paragraph("🔬 TÉCNICAS DE SELECCIÓN", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    tecnicas_data = [
        ["TÉCNICA", "APLICACIÓN"],
        ["1️⃣ Fenotípica", "Evaluación visual y medición de características observables"],
        ["2️⃣ Pedigrí", "Análisis genealógico para identificar líneas superiores"],
        ["3️⃣ Progenie", "Evaluación por desempeño de crías (más preciso)"],
        ["4️⃣ Molecular", "Marcadores genéticos y ADN (vanguardia)"]
    ]
    
    tabla_tec = Table(tecnicas_data, colWidths=[35*mm, 115*mm])
    tabla_tec.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_ACENTO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
        ('BOX', (0, 0), (-1, -1), 1, COLOR_PRIMARIO),
    ]))
    elementos.append(tabla_tec)
    elementos.append(Spacer(1, 6*mm))
    
    # Sistemas de empadre
    elementos.append(Paragraph("❤️ SISTEMAS DE EMPADRE", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "✓ <b>Controlado:</b> 1 macho + grupo hembras · Control pedigrí<br/>"
        "✓ <b>Dirigido:</b> Macho + hembra específicos complementarios<br/>"
        "✓ <b>Inseminación Artificial:</b> Semen élite en múltiples hembras<br/>"
        "✓ <b>Transferencia Embriones:</b> Multiplicar genética de alto valor",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 6*mm))
    
    # Parámetros de calidad - tabla mejorada
    elementos.append(Paragraph("📏 PARÁMETROS DE CALIDAD DE FIBRA", styles['Seccion']))
    elementos.append(Spacer(1, 3*mm))
    
    parametros = [
        ["PARÁMETRO", "OBJETIVO", "ESTÁNDAR"],
        ["Finura (micrones)", "< 22 μm", "Baby/Superfine"],
        ["Densidad", "Alta", "> fibras/cm²"],
        ["Longitud/año", "8-12 cm", "Óptimo"],
        ["Carácter", "Uniforme", "Ondulación definida"],
        ["Resistencia", "> 40 N/Ktex", "Alta tensión"],
        ["Color", "Uniforme", "Sin manchas"]
    ]
    
    tabla_param = Table(parametros, colWidths=[50*mm, 45*mm, 55*mm])
    tabla_param.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARIO),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_BLANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 1), (1, -1), 'CENTER'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_CLARO, COLOR_GRIS_CLARO]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_GRIS_MEDIO),
    ]))
    elementos.append(tabla_param)
    elementos.append(Spacer(1, 6*mm))
    
    # Manejo nutricional compacto
    elementos.append(Paragraph("🌱 NUTRICIÓN", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "🥗 Proteína 12-14% · ⚡ Energía calidad · 💎 Minerales (Cu, Zn, S) · "
        "💧 Agua libre acceso · 🔄 Pastoreo rotativo",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 6*mm))
    
    # Programa sanitario
    elementos.append(Paragraph("💊 SANIDAD", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "✓ Desparasitación cada 3-4 meses<br/>"
        "✓ Vacunación clostridiosis<br/>"
        "✓ Control sarna, piojo, garrapata<br/>"
        "✓ Vitaminas y minerales preventivos<br/>"
        "✓ Cuarentena animales nuevos<br/>"
        "✓ Inspección periódica estado corporal",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 6*mm))
    
    # Registros destacados
    elementos.append(Paragraph("📋 REGISTROS ESENCIALES", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "🏷️ Identificación individual · 🌳 Pedigrí completo · 📅 Nacimientos · "
        "⚖️ Peso periódico · 🧵 Calidad fibra · ❤️ Historial reproductivo · 🏥 Veterinario",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 6*mm))
    
    # Capacitación destacada
    elementos.append(Paragraph("🎓 CAPACITACIÓN EN FECASAM 2026", styles['Seccion']))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "Durante el evento se realizarán talleres sobre:",
        styles['Destacado']
    ))
    elementos.append(Spacer(1, 2*mm))
    elementos.append(Paragraph(
        "✓ Mejoramiento genético y biotecnologías<br/>"
        "✓ Innovación tecnológica en textiles<br/>"
        "✓ Manejo sostenible de pastizales<br/>"
        "✓ Sanidad y bioseguridad<br/>"
        "✓ Clasificación y comercialización<br/>"
        "✓ Normativas y certificación",
        styles['CuerpoTexto']
    ))
    elementos.append(Spacer(1, 7*mm))
    
    # Contacto final
    elementos.append(DecorativeLine(17*cm, COLOR_SECUNDARIO, 1))
    elementos.append(Spacer(1, 3*mm))
    elementos.append(Paragraph(
        "📧 fecasam2026@gmail.com | 📞 979 007 682",
        styles['CuerpoTexto']
    ))
    
    doc.build(elementos)
    print(f"✓ PDF creado: {filename}")

def main():
    """Función principal"""
    # Crear directorio si no existe
    output_dir = "assets/downloads"
    os.makedirs(output_dir, exist_ok=True)
    
    print("🎨 Creando PDFs con contenido real para FECASAM 2026...\n")
    
    # Crear estilos
    styles = crear_estilos()
    
    # Crear cada PDF
    print("📄 Generando documentos...\n")
    
    crear_programa_pdf(os.path.join(output_dir, "programa-fecasam-2026.pdf"), styles)
    crear_bases_concurso_pdf(os.path.join(output_dir, "bases-concurso.pdf"), styles)
    crear_ruta_paqochanan_pdf(os.path.join(output_dir, "ruta-paqochanan.pdf"), styles)
    crear_catalogo_expositores_pdf(os.path.join(output_dir, "catalogo-expositores.pdf"), styles)
    crear_manual_biotecnologia_pdf(os.path.join(output_dir, "manual-biotecnologia.pdf"), styles)
    
    print(f"\n✅ Se crearon 5 archivos PDF con contenido real en {output_dir}/")
    print("\n📋 Archivos generados:")
    print("   ✓ programa-fecasam-2026.pdf - Programa oficial del evento")
    print("   ✓ bases-concurso.pdf - Reglamento del concurso de alpacas")
    print("   ✓ ruta-paqochanan.pdf - Guía turística Ruta de la Alpaca")
    print("   ✓ catalogo-expositores.pdf - Información para expositores")
    print("   ✓ manual-biotecnologia.pdf - Manual de mejoramiento genético")

if __name__ == "__main__":
    main()
