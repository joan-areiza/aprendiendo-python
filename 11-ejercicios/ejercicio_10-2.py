def maximo(a, b):  # Define la función máximo con parámetros 'a' y 'b'.
    if a > b:  # Compara los parámetros recibidos.
        return a  # Retorna 'a' si es mayor.
    else:
        return b  # Retorna 'b' de lo contrario.


def minimo(a, b):  # Define la función mínimo con parámetros 'a' y 'b'.
    if a < b:  # Compara los parámetros recibidos.
        return a  # Retorna 'a' si es menor.
    else:
        return b  # Retorna 'b' de lo contrario.


# Programa principal
x = int(input("Un número: "))  # 5 - Recibe la variable de entrada x
y = int(input("Otro número: "))  # 1 - Recibe la variable de entrada y

# Evaluación:
# minimo(5+2, 1-5) -> minimo(7, -4) -> retorna -4
# maximo(5-3, -4)  -> maximo(2, -4) -> retorna 2
print(
    maximo(x - 3, minimo(x + 2, y - 5))
)  # Muestra el resultado de evaluar las funciones anidadas con las expresiones.
