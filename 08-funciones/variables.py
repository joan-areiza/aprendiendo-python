"""
Variables locales: se definen dentro de la función y no
se pueden usar fuera de ella, solo están disponibles dentro.

Variables globales: son las que se declaran fuera de una función
y estan disponibles dentro y fuera de ellas.
"""

# Variable Global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def holamundo():
    #frase = "Hola Mundo!!"
    print(frase)

holamundo()