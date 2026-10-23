def sumar_digitos(
    numero,
):  # Define la función para calcular la suma de los dígitos de un número[cite: 5].
    suma = 0  # Inicializa en cero el contador acumulado de la suma de dígitos[cite: 5].
    for digito in str(
        abs(numero)
    ):  # Recorre la representación en string del valor absoluto de 'numero'[cite: 5].
        suma += int(digito)  # Convierte el dígito a entero y lo suma a 'suma'[cite: 5].
    return suma  # Retorna el total acumulado de los dígitos[cite: 5].


sumatoria_numeros = 0  # Variable acumuladora para almacenar la suma total de los números ingresados[cite: 5].
sumatoria_digitos = 0  # Variable acumuladora para almacenar la suma total de todos los dígitos[cite: 5].

while True:  # Bucle infinito para lectura continua.
    num = int(
        input("Ingresa un número (0 para salir): ")
    )  # Pide un número al usuario.
    if num == 0:  # Condición para terminar la ejecución del bucle.
        break  # Finaliza la ejecución del ciclo.
    suma_d = sumar_digitos(num)  # Llama a la función y almacena su retorno.
    print(f"Suma de dígitos: {suma_d}")  # Muestra la suma del número actual.

    sumatoria_numeros += (
        num  # Suma el número ingresado a la sumatoria total de números.
    )
    sumatoria_digitos += suma_d  # Suma la suma de dígitos actual a la sumatoria total de dígitos.

print(
    f"\nSumatoria total de números ingresados: {sumatoria_numeros}"
)  # Imprime el total global acumulado de los números.
print(
    f"Sumatoria total de todos los dígitos: {sumatoria_digitos}"
)  # Imprime el total global acumulado de la suma de los dígitos.
