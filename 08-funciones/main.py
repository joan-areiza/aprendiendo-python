# función sin parámetros o retorno de valores
def diHola():
    print("Hello!")

diHola()  # llamada a la función, 'Hello!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
    print("Hello " + name + "!")

holaConNombre("Ada")  # llamada a la función, 'Hello Ada!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
    return val1 * val2

multiplica(3, 5)  # muestra 15 en la consola

# esta es una función básica de suma
def suma(a, b):
    return a + b

result = suma(1, 2)
# result = 3

def suma(a, b=3):
    return a + b

result = suma(1)
# result = 4

result = suma(b=2, a=2)
# result = 4

result = suma(3, b=2)
#result = 5


#result2 = suma(b=2, 3)
#Lanzará SyntaxError


s = suma
result = s(1, 2)
# result = 3

#print(multiplica(3))  # TypeError: multiplica() utiliza exactamente 2 argumentos (0 proporcionados)

print(multiplica('a', 5))  # 'aaaaa' mostrado en la consola

#print(multiplica('a', 'b'))  # TypeError: Python no puede multiplicar dos strings

def miFunción():
    print('this will print')
    print('so will this')

x = 7
# la asignación de x no es parte de la función ya que no está indentada

def duplica(num):
    x = num * 2
    return x

print(x)  # error - x no está definida
print(duplica(4))  # muestra 8

'''
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función cuantas veces como sea necesario. Ejemplo de sintaxis:
def nombreDeMiFuncion(parametros):
Bloque de codigo / conjunto de instrucciones
invocar
nombreDeMiFuncion(el_parametro)
'''

#Ejemplo 1
print(" ##### Ejemplo 1 #####")
#Definir función
def muestraNombre():
    print("Victor")
    print("Pedro")
    print("Juan")
    print("Felipe")
    print("Santiago")
    print("Sandra")
#invocar función
muestraNombre()

#Ejemplo 2 - Parametros
print(" ###### Ejemplo 2 PARAMETROS ######")

def mostrarTuNombre(nombre): #parametro
    print(f"Tu nombre es: {nombre}")

mostrarTuNombre("Carlos Perez")
mostrarTuNombre("Sandra Flores")
mostrarTuNombre("Juan Garcia")

#Ejemplo 2 - Parametros (con input)
print(" ###### Ejemplo 2 PARAMETROS ######")

def mostrarTuNombre(nombre): #parametro
    print(f"Tu nombre es: {nombre}")
nombre = input("Introduce tu nombre: ")
mostrarTuNombre(nombre)

#Ejemplo 2 - Parametros (con edad)
def mostrarTuNombre(nombre, edad): #parametro
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
mostrarTuNombre(nombre, 19)

#Ejemplo 3 PARAMETROS Tablas de Multiplicar
print(" ###### Ejemplo 3 PARAMETROS Tablas de Multiplicar ######")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    
    for contador in range(5):
        operacion = numero * contador
        print(f"{numero} X {contador} = {operacion}")
        
    print("\n") #salto de línea

tabla(3)
tabla(14)

#Ejemplo 4 - Parametros Opcionales
print(" ###### Ejemplo 4 PARAMETROS Opcionales ######")
def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Moises Garcia", 76327191)

#Ejemplo 5 - Parametros Opcionales y return o devolver datos de una función
print(" ###### Ejemplo 5 PARAMETROS Opcionales y return o devolver datos de una función ######")
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    cadena = ""
    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicación: " + str(multiplicacion)
    cadena += "\n"
    cadena += "División: " + str(division)
    cadena += "\n"
    return cadena

print(calculadora(5, 5))

#Ejemplo 5 modificado - Parametros Opcionales y return o devolver datos de una función
print(" ###### Ejemplo 5 PARAMETROS Opcionales y return o devolver datos de una función ######")
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multiplicacion)
        cadena += "\n"
        cadena += "División: " + str(division)
        cadena += "\n"
    return cadena

print(calculadora(10, 5, True))

#Ejemplo 6 - Uso de funciones dentro de una función
print(" ###### Ejemplo 6 Funciones dentro de una función ######")
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"El apellido es: {apellidos}"
    return texto

print(getNombre("Carlos"), getApellidos("Sanchez"))

#Ejemplo 6 - Uso de funciones en el mismo ejercicio
print(" ###### Ejemplo 6 Funciones dentro de una función ######")
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"El apellido es: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Jose", "Perez"))

#>>> lambda argumento1, argumento2, argumentoN : expresion usando argumentos 

#Ejemplo 7 - Función Lambda
print(" ###### Ejemplo 7 Función Lambda ######")
dime_el_year = lambda year: f"El año es {year}"
print(dime_el_year(2023))