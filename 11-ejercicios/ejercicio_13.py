def validar_dni(
    dni,
):  # Función encargada de validar que el DNI tenga solo números y entre 7 y 8 dígitos.
    dni_str = str(
        dni
    ).strip()  # Convierte a string y elimina espacios externos.
    return dni_str.isdigit() and len(dni_str) in (
        7,
        8,
    )  # Retorna True si es numérico y su longitud es 7 u 8.


def generar_identificador(
    nombre_completo, dni
):  # Función que genera el ID de socio a partir del nombre completo y el DNI.
    partes = (
        nombre_completo.strip().split()
    )  # Quita espacios bordes y divide el nombre completo en una lista de palabras.
    primer_nombre = partes[0]  # Extrae el primer nombre (índice 0).
    apellido = partes[-1]  # Extrae el último elemento (el apellido).

    cant_letras_apellido = len(
        apellido
    )  # Cuenta el número de caracteres del apellido.
    primeros_3_dni = str(dni)[
        :3
    ]  # Convierte el DNI a string y obtiene sus primeros 3 caracteres usando slicing [:3].

    return f"{primer_nombre}{cant_letras_apellido}{primeros_3_dni}"  # Une el primer nombre, la longitud del apellido y las 3 cifras del DNI.


# Bucle principal
while True:  # Ciclo infinito para pedir datos de socio indefinidamente.
    nombre = input(
        "\nIngresa el nombre completo del socio (o presiona Enter para salir): "
    )  # Lee el nombre completo.
    if (
        nombre.strip() == ""
    ):  # Condición de salida: si el usuario presiona Enter sin escribir texto.
        break  # Finaliza el bucle principal.

    while (
        True
    ):  # Bucle anidado para reintentar la captura del DNI hasta que sea válido.
        dni = input(
            "Ingresa el número de DNI (7 u 8 dígitos): "
        )  # Solicita el DNI del socio.
        if validar_dni(
            dni
        ):  # Si la función retorna True (es válido), se acepta.
            break  # Sale del bucle de validación de DNI.
        print(
            "DNI inválido. Debe contener únicamente entre 7 y 8 dígitos."
        )  # Notifica error y repite la solicitud.

    ID = generar_identificador(
        nombre, dni
    )  # Invoca la función para armar el identificador.
    print(
        f"Identificador único generado: {ID}"
    )  # Imprime el ID obtenido para el socio.
