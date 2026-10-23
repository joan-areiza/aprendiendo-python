# Comandos de la terminal
# cls/clean -> limpiar pantalla,
# cd -> cambiar de directorio,
# ls/dir -> listar archivos y carpetas,
# mkdir -> crear carpeta,
# touch -> crear archivo,
# rm -> eliminar archivo,
# rmdir -> eliminar carpeta,
# mv -> mover archivo o carpeta,
# cp -> copiar archivo o carpeta

# Comandos de ruta
# . -> ruta actual,
# .. -> ruta anterior,
# / -> ruta raiz,
# ../../ -> ruta dos niveles hacia atras

# mysql-connector-python
# pip install mysql-connector-python

import mysql.connector

# Conexion a la Base de datos
database = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="master_python"
)

# ¿La conexion ha sido correcta?
# print(database)

# Cursor que nos permite ejecutar las consultas
cursor = database.cursor(buffered=True)

"""
# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Mostrar las bases de datos creadas
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
"""

# Crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) AUTO_INCREMENT NOT NULL, 
    marca VARCHAR(40) NOT NULL, 
    modelo VARCHAR(40) NOT NULL, 
    precio FLOAT(10,2) NOT NULL,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
    """)

"""
#Mostrar las tablas creadas en la base de datos
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""

# Insertar registros en la tabla
# cursor.execute("INSERT INTO vehiculos VALUES (null, 'Open1', 'Astra', 18500)")

carros = [
    ("Seat", "Ibiza", 5000),
    ("Renault", "Clio", 15000),
    ("Citroen", "Saxo", 2000),
    ("Mercedes", "Clase C", 35000),
]

# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", carros)
database.commit()

# Listar informacion de la tabla o de la base de datos
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")
resultado = cursor.fetchall()
print("-------------------- TODOS MIS CARROS --------------------")
for carro in resultado:
    print(carro[1], carro[3])

cursor.execute("SELECT * FROM vehiculos")
carro = cursor.fetchone()
print(carro)

#Eliminar registros de la tabla
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "Borrados!!")

#Actualizar registros de la tabla
cursor.execute("UPDATE vehiculos SET modelo = 'León' WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, "Actualizados!!")