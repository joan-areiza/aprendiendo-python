import os

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# Eliminar carpeta
# os.rmdir("./mi_carpeta")
