# Importar modulo
import sqlite3

# Conexion a base de datos
conexion = sqlite3.connect("prueba.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255), 
    descripcion text, 
    precio int(255));
            """)

# Guardar los cambios
conexion.commit()

"""
# Insertar datos
cursor.execute(
    "INSERT INTO productos VALUES(null, 'Segundo producto', 'Descripciòn de mi producto', 800)"
)
conexion.commit()
"""

# Borrar registros
# cursor.execute("DELETE FROM productos")
# conexion.commit()

# Insertar muchos registros ala vez
productos = [
    ("Portatil", "15 Pulgadas", 700000),
    ("Telefono Movil", "iPhone", 250000),
    ("Procesador", "Core 7", 900000),
    ("Tablet", "10 Pulgadas", 500000),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

# Actualizar Update
cursor.execute("UPDATE productos SET precio = 600000 WHERE precio = 500000")

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio  <= 1000000;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripciòn: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

# Cerrar la conexiòn
conexion.close()
