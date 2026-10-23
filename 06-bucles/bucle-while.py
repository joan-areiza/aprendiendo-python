"""
#BUCLE WHILE
Estructura de control que itera o repite la ejerciòn de una serie de instrucciones tantas veces como sea necesario, hasta que deje de cumplirse la condiciòn.

contador
while condiciòn:
    Bloque de instrucciones
    actualizaciòn de contador
"""

contador = 1
while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

print("----------------------------------------")
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1
    print(muestrame)

# Ejemplo

print("### EJEMPLO ###")
numero_usuario = int(
    input("¿De que numero quieres la tabla: ?")
)  # Creacion de variable con parseo int
if numero_usuario < 1:  # Comprobar si numero de usuario es menor a 1
    numero_usuario = 1  # Le damos un valor de usuario que sera 1
print(f"### Tabla del {numero_usuario} ###")  # Se muestra la tabla de multiplicar
contador = 1  # Se define el contador
while (
    contador <= 10
):  # Mientras que el contador sea menor o igual a 10 sigue entrando el bucle
    print(
        f"{numero_usuario} x {contador} = {numero_usuario*contador}"
    )  # Muestra la multiplicaciòn
    contador += 1  # Actualizamos el contador para uno de factores
else:  # si no
    print("Tabla terminada.")  # Termina
