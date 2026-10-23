numero = 1  # Inicializa el multiplicando base en 1.

while numero <= 10:  # Bucle externo que recorre los números base del 1 al 10.

    print(
        f"\n********** TABLA DEL {numero} **********"
    )  # Imprime el encabezado de la tabla actual.

    multiplicador = 1  # Inicializa el multiplicador en 1 para cada tabla.

    while (
        multiplicador <= 10
    ):  # Bucle interno que va del 1 al 10 para multiplicar.

        resultado = (
            numero * multiplicador
        )  # Calcula el producto de los dos números.

        print(
            f"{numero} x {multiplicador} = {resultado}"
        )  # Muestra la operación con su resultado.

        multiplicador += 1  # Incrementa el multiplicador en 1.

    numero += 1  # Incrementa el número base para pasar a la siguiente tabla.
