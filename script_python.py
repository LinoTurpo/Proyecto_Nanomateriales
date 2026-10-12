import cv2
import serial

# 1. Cargar y binarizar la imagen
imagen = cv2.imread('cuadrado.png', cv2.IMREAD_GRAYSCALE)
_, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

filas, columnas = imagen_binaria.shape
resolucion_mm = 0.01  # 10 micrometros
comandos_gcode = []

# 2. Recorrer píxeles y convertir a G-Code
for y in range(filas):
    for x in range(columnas):
        if imagen_binaria[y, x] == 0:  # Píxel negro 
            x_mm = x * resolucion_mm
            y_mm = y * resolucion_mm
            # Dar formato G-Code con 3 decimales
            comando = f"G1 X{x_mm:.3f} Y{y_mm:.3f}"
            comandos_gcode.append(comando)

# Mostrar los primeros 3 comandos de ejemplo
print("Ejemplo de comandos generados:")
for cmd in comandos_gcode[:3]:
    print(cmd)
    
# Guardar la lista de comandos en un archivo de texto
with open("patron_litografia.gcode", "w") as archivo:
    for comando in comandos_gcode:
        archivo.write(comando + "\n")

print("¡Archivo patron_litografia.gcode creado con éxito!")
