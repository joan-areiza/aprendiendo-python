import math  # Importa la librería matemática para el factorial.


def es_primo(numero):  # Función que determina si un número es primo.
    if numero <= 1:  # Menores o iguales a 1 no son primos.
        return False  # Retorna False.
    for i in range(
        2, int(numero**0.5) + 1
    ):  # Explora divisores potenciales hasta la raíz cuadrada.
        if numero % i == 0:  # Si tiene división exacta no es primo.
            return False  # Retorna False.
    return True  # Si no tiene divisores es primo, retorna True.


def sumar_digitos(
    numero,
):  # Función para sumar los dígitos individuales de un número.
    return sum(
        int(d) for d in str(abs(numero))
    )  # Suma cada dígito convertido a entero.


def frecuencia_digito(
    numero, digito
):  # Función para contar cuántas veces se repite un dígito.
    return str(abs(numero)).count(
        str(digito)
    )  # Cuenta las ocurrencias en la versión string.


digito_buscar = int(
    input("Ingresa el dígito que deseas rastrear (0-9): ")
)  # Lee el dígito objetivo a rastrear.
mayor_primo = None  # Almacena el primo más grande ingresado.

while True:  # Bucle principal de lectura.
    num = int(input("\nIngresa un número primo: "))  # Solicita un número.
    if not es_primo(
        num
    ):  # Evalúa la condición de corte: interrumpe si NO es primo.
        print(
            f"El número {num} no es primo. Finalizando lectura..."
        )  # Avisa el fin de lectura.
        break  # Detiene el ciclo.

    if (
        mayor_primo is None or num > mayor_primo
    ):  # Compara e identifica el mayor primo hasta el momento.
        mayor_primo = num  # Guarda el nuevo primo mayor.

    print(
        f"Suma de dígitos: {sumar_digitos(num)}"
    )  # Muestra la suma de dígitos.
    print(
        f"Frecuencia del dígito {digito_buscar}:"
        f" {frecuencia_digito(num, digito_buscar)}"
    )  # Muestra las ocurrencias.

if (
    mayor_primo is not None
):  # Verifica si se procesó exitosamente al menos un primo.
    print(
        f"\nEl mayor número primo ingresado fue {mayor_primo}."
    )  # Muestra el primo máximo.
    print(
        f"Su factorial es: {math.factorial(mayor_primo)}"
    )  # Calcula y muestra su factorial.
else:
    print(
        "\nNo se ingresó ningún número primo."
    )  # Mensaje en caso de ingresar un no primo en la primera entrada.
