def longitud_ultima_palabra(
    cadena,
):  # Define la función 'longitud_ultima_palabra' que acepta un texto 'cadena'.
    palabras = (
        cadena.strip().split()
    )  # Elimina espacios iniciales/finales con .strip() y divide la cadena por espacios con .split() creando una lista de palabras.
    if (
        not palabras
    ):  # Si la lista 'palabras' está vacía (por ejemplo, si la entrada eran solo espacios):
        return 0  # Retorna una longitud de 0.
    return len(
        palabras[-1]
    )  # Accede a la última palabra mediante el índice [-1] y retorna su cantidad de caracteres usando len().
