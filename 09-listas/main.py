"""
Listas(arrays) son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numereico.
"""

# Definir una lista
"""
#Definir una tupla (inmutable)
cantantes = list(('Maelo','Marck','Jennifer Lopez'))
print(cantantes)

#Definir una lista con range
years = list(range(2024, 2050))
print(years)

#Definir una lista variada
variada = ["Victor", 30, 4.4, True, "Texto"]
print(variada)

# Indices
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
peliculas[1] = "La gran estafa"
print(peliculas[1])
print(peliculas[-2])

# Recorre indices[Desde:Hasta(sin empezar por cero)]
print(peliculas[1:3])
print(peliculas[0:2])
print(peliculas[0:])

# Añadir elementos a una lista
peliculas.append("El hobbit")
print(peliculas)

# Recorrer una lista
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n**********Listado de Peliculas**********")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
"""

# Listas Multidimensionales
print("\n**********Listado de Contactos**********")
contactos = [
    ["Carlos", "carlos@gmail.com"],
    ["Luis", "luis@gmail.com"],
    ["Sandra", "sandra@gmail.com"],
]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#print(contactos[1][1])
