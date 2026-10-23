estudiante = 1  # Contador de control para el número de estudiante actual.
aprobados = 0  # Contador acumulativo para estudiantes aprobados.
perdidos = 0  # Contador acumulativo para estudiantes reprobados/perdidos.

while estudiante <= 15:  # Bucle condicionado hasta procesar 15 estudiantes.

    nota = float(
        input(f"Ingrese la nota del estudiante {estudiante}: ")
    )  # Pide la nota como número flotante.

    if (
        nota >= 3.0
    ):  # Evalúa el criterio de aprobación (nota mayor o igual a 3.0).
        aprobados += 1  # Incrementa el contador de aprobados.
    else:
        perdidos += 1  # Incrementa el contador de perdidos.

    estudiante += 1  # Pasa al siguiente estudiante.

print(
    f"\nCantidad de estudiantes aprobados: {aprobados}"
)  # Imprime el total de aprobados.
print(
    f"\nCantidad de estudiantes perdidos: {perdidos}"
)  # Imprime el total de perdidos.
