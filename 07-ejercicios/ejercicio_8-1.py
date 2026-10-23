porcentaje = float(
    input("Ingrese el porcentaje: ")
)  # Pide la tasa porcentual deseada.
numero = float(
    input("Ingrese el numero: ")
)  # Pide la cantidad base a calcular.

resultado = (
    porcentaje * numero
) / 100  # Aplica la fórmula estándar de porcentaje.

print(
    f"\nEl {porcentaje}% de {numero} es: {resultado}"
)  # Imprime el resultado obtenido.
