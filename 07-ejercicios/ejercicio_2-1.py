n = 5  # Inicializa la variable de control 'n' en 5.

while (
    n <= 110
):  # Mantiene el ciclo activo mientras 'n' sea menor o igual a 110.
    if (
        n % 2 == 0
    ):  # Evalúa si el residuo de 'n' dividido entre 2 es 0 (es decir, si es par).
        print(n)  # Imprime el valor de 'n' si cumple la condición de ser par.
    n += 1  # Incrementa en 1 el valor de 'n' para avanzar en cada iteración.
