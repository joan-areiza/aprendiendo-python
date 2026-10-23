def calcular_frecuencia(
    numero, digito
):  # Define la función que acepta 'numero' y 'digito' como parámetros.
    return str(abs(numero)).count(
        str(digito)
    )  # Convierte ambos a string y usa .count() para contar la frecuencia del dígito.


num = int(
    input("Ingresa un número entero: ")
)  # Solicita al usuario el número entero de análisis.
dig = int(
    input("Ingresa el dígito a buscar (0-9): ")
)  # Solicita el dígito específico cuyo conteo se requiere.

frecuencia = calcular_frecuencia(
    num, dig
)  # Invoca la función pasando los valores ingresados.
print(
    f"El dígito {dig} aparece {frecuencia} vez/veces en {num}."
)  # Despliega el resultado formateado.
