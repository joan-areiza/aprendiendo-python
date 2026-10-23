numero_uno = int(
    input("Ingrese el primer numero: ")
)  # Lee y convierte a entero el primer número.
numero_dos = int(
    input("Ingrese el segundo numero: ")
)  # Lee y convierte a entero el segundo número.

print(
    f"\nNumeros entre {numero_uno} y {numero_dos}:"
)  # Imprime un mensaje informativo indicando el rango.

if (
    numero_uno < numero_dos
):  # Evalúa si el primer número es menor que el segundo.
    for numero in range(
        numero_uno, numero_dos + 1
    ):  # Genera el rango ascendente desde numero_uno hasta numero_dos.
        print(numero)  # Imprime el valor actual dentro del rango.
else:  # Caso en el que el segundo número sea menor o igual al primero.
    for numero in range(
        numero_dos, numero_uno + 1
    ):  # Genera el rango de menor a mayor (numero_dos hasta numero_uno).
        print(numero)  # Imprime el valor actual dentro del rango.
