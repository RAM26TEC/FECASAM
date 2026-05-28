#!/usr/bin/env python3
"""
Script para crear un favicon limpio basado en el logo oficial.
Solo el logo sin fondo ni borde.
"""

from PIL import Image, ImageFilter
import os

def crear_favicon_limpio(logo_path, output_path, tamanios=[16, 32, 48, 64, 128, 256]):
    """
    Crea un favicon limpio solo con el logo, sin fondo ni borde.
    
    Args:
        logo_path: Ruta al logo original
        output_path: Ruta de salida para el favicon
        tamanios: Lista de tamaños a generar
    """
    
    try:
        # Cargar el logo original
        logo = Image.open(logo_path)
        
        # Convertir a RGBA si no lo está
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Crear versiones en diferentes tamaños
        for size in tamanios:
            # Redimensionar logo manteniendo proporción y transparencia
            logo_resized = logo.copy()
            logo_resized.thumbnail((size, size), Image.Resampling.LANCZOS)
            
            # Para tamaños pequeños, aplicar sharpening para mejor claridad
            if size <= 48:
                logo_resized = logo_resized.filter(ImageFilter.SHARPEN)
            
            output_file = output_path.replace('.png', f'-{size}.png')
            logo_resized.save(output_file, 'PNG', optimize=True)
            print(f"✓ Favicon {size}x{size} creado: {output_file}")
        
        # Crear el favicon principal (32x32 es el estándar)
        favicon_32 = Image.open(output_path.replace('.png', '-32.png'))
        favicon_32.save(output_path, 'PNG', optimize=True)
        print(f"✓ Favicon principal creado: {output_path}")
        
        # Crear ICO multi-resolución (16, 32, 48)
        ico_path = output_path.replace('.png', '.ico')
        favicon_16 = Image.open(output_path.replace('.png', '-16.png'))
        favicon_32 = Image.open(output_path.replace('.png', '-32.png'))
        favicon_48 = Image.open(output_path.replace('.png', '-48.png'))
        
        favicon_16.save(
            ico_path,
            format='ICO',
            sizes=[(16, 16), (32, 32), (48, 48)],
            append_images=[favicon_32, favicon_48]
        )
        print(f"✓ Favicon .ico multi-resolución creado: {ico_path}")
        
        print("\n✅ Todos los favicons han sido creados exitosamente!")
        print(f"\n✓ Favicon limpio (solo logo, sin marco)")
        print(f"✓ Todos los tamaños generados con transparencia")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al crear favicon: {str(e)}")
        return False

if __name__ == "__main__":
    # Rutas de los archivos
    logo_path = "assets/images/logo-oficial2.png"
    output_path = "assets/images/favicon.png"
    
    print("🎨 Creando favicon limpio (solo logo)...")
    print(f"📂 Logo origen: {logo_path}")
    print(f"📂 Favicon destino: {output_path}\n")
    
    if not os.path.exists(logo_path):
        print(f"❌ Error: No se encuentra el archivo {logo_path}")
        exit(1)
    
    # Crear el favicon limpio
    crear_favicon_limpio(logo_path, output_path)
