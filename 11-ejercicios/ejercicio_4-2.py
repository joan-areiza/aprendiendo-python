def es_primo(
    numero,
):  # Define la función 'es_primo' que recibe un parámetro entero 'numero'.
    if numero <= 1:  # Caso base: números menores o iguales a 1 no son primos.
        return False  # Retorna False.
    for i in range(
        2, int(numero**0.5) + 1
    ):  # Itera desde 2 hasta la raíz cuadrada entera de 'numero' + 1.
        if (
            numero % i == 0
        ):  # Si el residuo de 'numero' dividido entre 'i' es 0, no es primo.
            return (
                False  # Retorna False inmediatamente si encuentra un divisor.
            )
    return True  # Si no encontró ningún divisor, confirma que el número es primo retornando True.


num = int(
    input("Ingresa un número entero: ")
)  # Solicita un número entero al usuario.
if es_primo(num):  # Evalúa la respuesta enviada por la función 'es_primo'.
    print(f"El número {num} es primo.")  # Mensaje en caso afirmativo.
else:
    print(f"El número {num} no es primo.")  # Mensaje en caso negativo.
