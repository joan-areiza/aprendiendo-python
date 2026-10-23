def validar_dni(
    dni,
):  # Define la función 'validar_dni' recibiendo 'dni' como parámetro.
    dni_str = str(
        dni
    ).strip()  # Convierte 'dni' a cadena de texto y elimina espacios en blanco al inicio o al final con .strip().
    return dni_str.isdigit() and len(dni_str) in (
        7,
        8,
    )  # Verifica que todos los caracteres sean dígitos (.isdigit()) Y que su cantidad de caracteres sea 7 u 8.
