"""
Una variable es un contenedor de informaciòn que dentro guradarà un dato,
se pueden crear muchas variables y que cada una tenga un dato distinto.
"""

# Crear variables y asignarlas en un valor
texto = "SENA formaciòn en Python"
texto_dos = "Joan Areiza"
numero = "40"
decimal = "7.6"

# Mostrar el valor de las variables
print(texto)
print(texto_dos)
print(numero)
print(decimal)

print("----------------------------------------")

# Sustituir el valor de algunas variables / reasignando valores
numero = "20"
decimal = "13.2"

# Mostrar el valor de las variables
print(numero)
print(decimal)

# Concatenaciòn
nivel = "TECNÒLOGO"
nombre = "ADSO"
centro = "Agropecuario"

print(nivel + " " + nombre + " - " + centro)
print("----------------------------------------")

# Usando la f y las { } obtenemos el mismo resultado
print(f"{nivel} {nombre} - {centro}")
print("----------------------------------------")

# Otra manera es usando el método .format {} y el nombre de las variables
print("Hola soy {} {} y mi centro de formaciòn es: {}".format(nivel, nombre, centro))
