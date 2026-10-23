"""
#Estructura de control que me permite controlar el flujo del programa condicional if

SI se_cumple_esta_condiciòn:
    Ejecutar grupo de instrucciones
SI NO
    Se ejecutan otro grupo de instrucciones en python

if condiciòn:
    instrucciones
else:
    otras instrucciones
"""

# Ejemplo 1
print("----------------------------------------")
print("########## EJEMPLO 1 #########")
color = "azul"

# Operador de comparaciòn ==
if color == "azul":
    print("El color es AZUL")
else:
    print("El color NO es AZUL")

# Color = "Azul"
# Operador de comparaciòn ==
color = input("Adivina cual es mi color favorito: ")
if color == "azul":
    print("El color es AZUL")
else:
    print("Color incorrecto!! ")

# Operadores de comparación
"""
== (igual que) a == b Se cumple si 'a' es igual que 'b'
!= (distinto a) a != b Se cumple si 'a' es distinto que 'b'
< (menor que) a < b Se cumple si 'a' es menor que 'b'
> (mayor que) a > b Se cumple si 'a' es mayor que 'b'
<= (menor o igual que) a <= b Se cumple si 'a' es menor o igual que 'b'
>= (mayor o igual que) a => b Se cumple si 'a' es mayor o igual que 'b'
"""

print("----------------------------------------")
print("\n########## EJEMPLO 2 ##########")
# year = 2021 #Variable que me compare el año
year = int(input("¿En que año estamos?"))

if year >= 2020:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un año anterior al 2021")

print("----------------------------------------")
print("\n########## EJEMPLO 3 ##########")
nombre = "Joan Areiza"
ciudad = "Popayàn"
continente = "America"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    # Instrucciones
    print(f"{nombre} es mayor que edad!!")
    if continente != "America":
        print("El usuario No es Americano")
    else:
        print(f"Es Americano y de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")

print("----------------------------------------")
print("\n########## EJEMPLO 4 ##########")
dia = int(input("Introduce el nùmero del dia de la semana "))

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia == 6:
                        print("Es sabado")
                    else:
                        if dia == 7:
                            print("Es domingo")          
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")

# Operadores lógicos y múltiples condiciones:
# a and b '¿Se cumple a y b?' 5==5 and b==1 #b=1... verdadero,
# z == 8 and 10==10 #z=9.. falso

# a or b  '¿Se cumple a o b?' 5==5 or b==1 #b=8.. verdadero,
# z==7 and 10==8 #z=7... falso

# not a 'No a' not(b==1) #b=5... verdadero,
# not(10==10) #falso

print("----------------------------------------")
print("\n########## EJEMPLO 5 ##########")
edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("¿Tienes edad de trabajar? Digite su edad !! "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !! ")
else:
    print("NO esta en edad de trabajar !! ")

print("----------------------------------------")
print("\n########## EJEMPLO 6 ##########")
pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !! ")
else:
    print(f"{pais} NO es un pais de habla hispana !! ")

print("----------------------------------------")
print("\n########## EJEMPLO 7 ##########")
pais = "Colombia"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} No es un pais de habla hispana !! ")
else:
    print(f"{pais} Si es un pais de habla hispana !! ")

print("----------------------------------------")
print("\n########## EJEMPLO 8 ##########")
pais = "España"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} No es un pais de habla hispana !! ")
else:
    print(f"{pais} Si es un pais de habla hispana !! ")
