"""
Modulos: Son funcionalidades ya hechas para reutilizar.

En Python hay muchos modulos, los podemos consultar aquì:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos.
"""

"""
# Importar modulo propio
# import mimodulo
#from mimodulo import holaMundo

# print(mimodulo.holaMundo("Carlos ADSO"))
# print(mimodulo.suma)

#print(holaMundo("Carlos ADSO"))

# Modulo fecha
import datetime 

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print("Mi fecha personalizada es: ", fecha_personalizada)

print(datetime.datetime().timestamp())


# Modulo de matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Numero pi: ", math.pi)

print("Redondear: ", math.floor(6.854875))
"""
# Modulo random

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))

