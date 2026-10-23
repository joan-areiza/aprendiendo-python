from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir en un archivo
archivo.write(
    "********************Soy un texto metido desde Python********************\n"
)

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print("- " + frase.upper())

# Copiar archivo
'''
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)


# Mover un archivo 
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"

shutil.move(ruta_original, ruta_nueva)
'''

#Eliminar
import os 

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"
os.remove(ruta_nueva)