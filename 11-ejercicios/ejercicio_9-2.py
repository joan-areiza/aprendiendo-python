def coordenadaZ(
    x, y
):  # Define la función 'coordenadaZ' que acepta dos parámetros 'x' e 'y'.
    x = x + 10  # Modifica localmente 'x' sumándole 10.
    y = y + 15  # Modifica localmente 'y' sumándole 15.
    return x + y  # Retorna la suma de las variables modificadas localmente.


# programa principal
x = int(input("Coordenada eje x: "))  # Lee el valor global inicial de x.
y = int(input("Coordenada eje y: "))  # Lee el valor global inicial de y.
for i in range(3):  # Bucle que se repite 3 veces (i = 0, 1, 2).
    z = coordenadaZ(
        x, y
    )  # Ejecuta la función pero no reasigna x ni y globales con el retorno.
    x = x + 1  # Incrementa la variable global x en 1.
    y = y + 1  # Incrementa la variable global y en 1.
print(
    x, " . ", y
)  # Muestra los valores finales de las variables globales x e y.
