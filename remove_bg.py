"""
Script para eliminar el fondo blanco del logo y convertirlo a PNG transparente
"""
from PIL import Image
import sys

def remove_white_background(input_path, output_path, threshold=240):
    """
    Elimina el fondo blanco de una imagen y la convierte a PNG con transparencia
    
    Args:
        input_path: Ruta de la imagen de entrada
        output_path: Ruta de la imagen de salida
        threshold: Umbral para considerar un pixel como blanco (0-255)
    """
    try:
        # Abrir la imagen
        img = Image.open(input_path)
        
        # Convertir a RGBA si no lo está
        img = img.convert("RGBA")
        
        # Obtener datos de píxeles
        datas = img.getdata()
        
        # Crear nueva lista de píxeles
        new_data = []
        
        for item in datas:
            # Si el pixel es blanco (o casi blanco), hacerlo transparente
            # Verificamos que R, G y B sean mayores al umbral
            if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                # Hacer transparente (alpha = 0)
                new_data.append((255, 255, 255, 0))
            else:
                # Mantener el pixel original
                new_data.append(item)
        
        # Actualizar datos de imagen
        img.putdata(new_data)
        
        # Guardar como PNG
        img.save(output_path, "PNG")
        
        print(f"✓ Logo procesado exitosamente")
        print(f"  Entrada: {input_path}")
        print(f"  Salida: {output_path}")
        print(f"  Fondo blanco eliminado con threshold={threshold}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error al procesar imagen: {e}")
        return False

if __name__ == "__main__":
    # Rutas de archivos
    input_logo = r"d:\2026\SISTEMAS\FECASAM 2026\imgs\logo Fecasam 2026.jpeg"
    
    # Procesar logo con diferentes umbrales para mejor resultado
    outputs = [
        (r"d:\2026\SISTEMAS\FECASAM 2026\assets\images\logo.png", 240),
        (r"d:\2026\SISTEMAS\FECASAM 2026\assets\images\logo-light.png", 240),
        (r"d:\2026\SISTEMAS\FECASAM 2026\assets\images\favicon.png", 240)
    ]
    
    print("\n=== Eliminando fondo blanco del logo ===\n")
    
    for output_path, threshold in outputs:
        remove_white_background(input_logo, output_path, threshold)
        print()
    
    print("=== Proceso completado ===")
