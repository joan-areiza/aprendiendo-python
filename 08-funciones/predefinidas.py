nombre = "ADSI SENA AgroTics"

#Funciones Generales
print(type(nombre))

#Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un String")
else:
    print("Esa variable NO es un String")
    
if not isinstance(nombre, float):
    print("Esa variable NO es un numero con decimales")

#Limpiar espacios de un String
frase = "     mi contenido     "
print(frase)
print(frase.strip())

#Eliminar variable
year = 2022
print(year)
del year
#print(year)

#Comprobar variable vacia
texto = "  fff  "
if len(texto) <= 0 :
    print("La variable esta vacia")
else:
    print("La variable tiene contenido: ", len(texto))

#Encontrar caracteres en un texto
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Mayusculas y Minusculas
print(frase)
print(frase.lower())
print(frase.upper())

def suma(a, b):
    x = a + b
    print(("Resultado", (x)))
suma(2, 3)

"""
1. FUNCIONES DE CADENAS EN PYTHON
---------------------------------
- print()   → Imprime en pantalla el argumento.
- len()     → Determina la longitud en caracteres de una cadena.
- join()    → Convierte una lista en cadena utilizando una separación.
- split()   → Convierte una cadena con un separador en una lista.
- replace() → Reemplaza una cadena por otra.
- upper()   → Convierte una cadena en Mayúsculas.
- lower()   → Convierte una cadena en Minúsculas.

2. FUNCIONES NUMÉRICAS EN PYTHON
--------------------------------
- range() → Crea un rango de números.
- str()   → Convierte un valor numérico a texto.
- int()   → Convierte a valor entero.
- float() → Convierte un valor a decimal.
- max()   → Determina el máximo entre un grupo de números.
- min()   → Determina el mínimo entre un grupo de números.
- sum()   → Suma el total de una lista de números.

3. OTRAS FUNCIONES ÚTILES EN PYTHON
-----------------------------------
- list()  → Crea una lista a partir de un elemento.
- tuple() → Crea o convierte en una tupla.
- open()  → Abre, crea, edita un elemento (archivo).
- ord()   → Devuelve el valor ASCII de una cadena o carácter.
- round() → Redondea después de la coma de un decimal.
- type()  → Devuelve el tipo de un elemento.
- input() → Permite la entrada de datos al usuario en Python 3.
"""