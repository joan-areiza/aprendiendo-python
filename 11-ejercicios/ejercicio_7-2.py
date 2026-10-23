def sumar_digitos(numero):  # Define la función de suma de dígitos.
    return sum(
        int(d) for d in str(numero)
    )  # Convierte el número a texto y suma sus dígitos convertidos a entero.


mayor_sumatoria = -1  # Registra la suma de dígitos más alta encontrada.
numero_mayor_sumatoria = (
    None  # Almacena el número que generó la suma más alta.
)
cantidad_menor_10 = (
    0  # Contador de números cuya suma de dígitos fue menor a 10.
)

while True:  # Bucle de captura continua.
    num = int(
        input("Ingresa un número positivo (negativo o 0 para finalizar): ")
    )  # Pide un entero.
    if num <= 0:  # Detiene la lectura si el número no es positivo.
        break  # Abandona el bucle.

    suma_d = sumar_digitos(num)  # Llama a la función sumar_digitos.

    if (
        suma_d > mayor_sumatoria
    ):  # Verifica si la suma actual supera el récord almacenado.
        mayor_sumatoria = suma_d  # Actualiza la mayor sumatoria.
        numero_mayor_sumatoria = num  # Guarda el número asociado.

    if suma_d < 10:  # Verifica si la suma de dígitos es menor a 10.
        cantidad_menor_10 += 1  # Incrementa el contador.

if (
    numero_mayor_sumatoria is not None
):  # Valida si se procesó al menos un número válido.
    print(
        f"\nEl número con la mayor suma de dígitos fue: {numero_mayor_sumatoria}"
        f" (suma: {mayor_sumatoria})"
    )  # Imprime el ganador.
    print(
        "Cantidad de números cuya suma de dígitos fue menor a 10:"
        f" {cantidad_menor_10}"
    )  # Imprime el conteo.
else:
    print(
        "No se ingresaron números válidos."
    )  # Notifica si se ingresó <= 0 desde el inicio.
