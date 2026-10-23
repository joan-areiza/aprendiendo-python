numero_uno = int(
    input("Ingrese el primer numero: ")
)  # Recibe el limite inferior.
numero_dos = int(
    input("Ingrese el segundo numero: ")
)  # Recibe el limite superior.

print(
    f"\nNumeros impares entre {numero_uno} y {numero_dos}:"
)  # Mensaje informativo del rango.

while (
    numero_uno <= numero_dos
):  # Se ejecuta mientras el primer número sea menor o igual al segundo.

    if (
        numero_uno % 2 != 0
    ):  # Evalúa si el número actual es impar (residuo de la división por 2 diferente de 0).
        print(numero_uno)  # Imprime el número impar.

    numero_uno += 1  # Incrementa en 1 el contador del rango.
