# Declaración de variables
municipio = input(
    "Ingrese el municipio: "
)  # Solicita al usuario el nombre del municipio y lo guarda en 'municipio'.
departamento = input(
    "Ingrese el departamento: "
)  # Solicita el nombre del departamento y lo guarda en 'departamento'.
year = str(
    input("Ingrese el año: ")
)  # Lee la entrada del usuario y la asegura explícitamente como tipo string (str) en 'year'.

print(
    f"El municipio es: {municipio}, El departamento es: {departamento}, El año es: {year}"
)  # Imprime un mensaje usando una f-string que interpola las tres variables[cite: 10].

print(
    type(municipio), type(year), type(departamento)
)  # Muestra en consola el tipo de dato de cada una de las variables creadas.
