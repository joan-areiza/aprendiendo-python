import math  # Importa el módulo matemático para usar la función factorial.


def calcular_factorial(
    n,
):  # Define la función para obtener el factorial de n.
    return math.factorial(
        n
    )  # Retorna el factorial de n calculado por math.factorial.


total_leidos = 0  # Contador de números procesados correctamente.

while True:  # Ciclo indeterminado para solicitar valores.
    entrada = input(
        "Ingresa un número entero no negativo (o 'fin' para salir): "
    )  # Recibe el dato ingresado por el usuario.
    if (
        entrada.lower() == "fin"
    ):  # Convierte a minúscula y valida si se escribió 'fin'.
        break  # Sale del ciclo de lectura.

    num = int(entrada)  # Convierte la entrada textual a número entero.
    if num < 0:  # Valida que el número no sea negativo.
        print(
            "El factorial no está definido para números negativos."
        )  # Advierte si es negativo.
        continue  # Salta a la siguiente iteración del ciclo.

    print(
        f"El factorial de {num} es: {calcular_factorial(num)}"
    )  # Imprime el resultado del factorial.
    total_leidos += 1  # Incrementa el contador global de lecturas.

print(
    f"\nCantidad total de números leídos: {total_leidos}"
)  # Muestra el total global de números leídos.
