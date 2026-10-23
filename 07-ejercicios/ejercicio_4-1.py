while True:  # Bucle principal para reiniciar o repetir operaciones.

    numero_uno = float(
        input("\nIngrese el primer numero: ")
    )  # Solicita el primer operando como flotante.
    numero_dos = float(
        input("Ingrese el segundo numero: ")
    )  # Solicita el segundo operando como flotante.

    print(
        "\n******************** CALCULADORA ********************"
    )  # Despliega encabezado.
    print("1. Suma")  # Opción 1 del menú.
    print("2. Resta")  # Opción 2 del menú.
    print("3. Multiplicacion")  # Opción 3 del menú.
    print("4. Division")  # Opción 4 del menú.

    operacion = int(
        input("Seleccione una operacion: ")
    )  # Captura la opción del usuario como número entero.

    if operacion == 1:  # Evalúa si la opción seleccionada es 1 (Suma).
        suma = (
            numero_uno + numero_dos
        )  # Realiza la adición entre los operandos.
        print(f"La suma es: {suma}")  # Imprime la suma resultante.

    elif operacion == 2:  # Evalúa si la opción seleccionada es 2 (Resta).
        resta = numero_uno - numero_dos  # Realiza la sustracción.
        print(f"La resta es: {resta}")  # Imprime la resta resultante.

    elif (
        operacion == 3
    ):  # Evalúa si la opción seleccionada es 3 (Multiplicación).
        multiplicacion = numero_uno * numero_dos  # Realiza el producto.
        print(
            f"La multiplicacion es: {multiplicacion}"
        )  # Imprime la multiplicación.

    elif operacion == 4:  # Evalúa si la opción seleccionada es 4 (División).
        if (
            numero_dos != 0
        ):  # Valida que el divisor no sea cero para evitar error.
            division = numero_uno / numero_dos  # Calcula la división exacta.
            residuo = (
                numero_uno % numero_dos
            )  # Calcula el residuo/módulo de la división.

            print(
                f"La division es: {division}"
            )  # Imprime el cociente obtenido.
            print(
                f"El residuo de la division es: {residuo}"
            )  # Imprime el módulo/residuo resultante.
        else:
            print(
                "No se puede dividir entre 0"
            )  # Notifica error de división por cero.

    else:
        print(
            "\nOperación no valida. Seleccione 1 o 4."
        )  # Notifica si se ingresó una opción inválida fuera del rango del menú.

    while (
        True
    ):  # Bucle interno para controlar si el usuario desea hacer otra operación.
        print("\n¿Desea realizar otra operacion?")  # Pregunta de confirmación.
        print("1. Si")  # Opción continuar.
        print("2. No")  # Opción salir.

        repetir = int(
            input("Seleccione una opcion: ")
        )  # Lee la selección del usuario.

        if repetir == 1:  # Opción 'Si'.
            break  # Rompe el bucle interno y vuelve a empezar el bucle principal de la calculadora.

        elif repetir == 2:  # Opción 'No'.
            print("Calculadora finalizada.")  # Mensaje de cierre.
            exit()  # Detiene la ejecución completa del programa.

        else:
            print(
                "\nOpcion no valida. Seleccione 1 o 2."
            )  # Mensaje de error para entradas no válidas en la confirmación.
