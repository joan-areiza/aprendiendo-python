"""
Diccionario: es un tipo de dato que almacena un conjunto de datos.
en formato clave -> valor
Es parecido a un array asociativo o un objeto json
"""

persona = {"nombre": "Carlos", "apellidos": "Paz", "correo": "carlospaz@gmail.com"}

# print(persona["correo"])
# Lista con diccionarios
contactos = [
    {"nombre": "Juan", "email": "juan@gmail.com"},
    {"nombre": "Carlos", "email": "carlos@gmail.com"},
    {"nombre": "Pedro", "email": "pedro@gmail.com"},
]
contactos[0]["nombre"] = "Juancito"
print(contactos[0]["nombre"])

print("\nListado de contactos: ")
print("------------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------------------------------")
