import sys
import re

def detectar_palabras_repetidas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            ultima_palabra = None
            for numero_linea, linea in enumerate(archivo, start=1):
                palabras = re.findall(r'\b\w+\b', linea.lower())
                
                for palabra in palabras:
                    if palabra == ultima_palabra:
                        print(f"Línea {numero_linea}: Palabra repetida -> '{palabra}'")
                    
                    ultima_palabra = palabra

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.", file=sys.stderr)
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.", file=sys.stderr)
    except Exception as e:
        print(f"Ocurrió un error inesperado al procesar el archivo: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: No se proporcionó el nombre del archivo.", file=sys.stderr)
        print("Uso correcto: python script.py <nombre_del_archivo>", file=sys.stderr)
        sys.argv = [sys.argv[0], "archivo.txt"] # Ejemplo de respaldo o salida limpia
    else:
        detectar_palabras_repetidas(sys.argv[1])
        