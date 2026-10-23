# ============================================================================
# 1. OPERADORES ARITMÉTICOS (Valores de ejemplo: a = 5; b = 10)
# ============================================================================

# +   -> Suma                            Ejemplo: a + b = 15
# -   -> Resta                           Ejemplo: b - a = 5
# *   -> Multiplicación o producto        Ejemplo: a * b = 50
# /   -> División                        Ejemplo: b / a = 2
# %   -> Módulo - Devuelve el resto      Ejemplo: b % a = 0
#        de la división
# **  -> Exponente - Realiza             Ejemplo: b ** a = 100000
#        exponencial
# //  -> División baja - Devuelve el    Ejemplo: b // a = 2
#        entero de la división


# ============================================================================
# 2. DATOS COMPUESTOS
# ============================================================================

"""
+----------------------------------------------------------------------------+
| Listas                                                                     |
+----------------------------------------------------------------------------+
| Sintaxis:          [e1, e2, e3]                                            |
| Constructores:     list(iterable)                                          |
| Orden:             Ordenados                                               |
| Duplicados:        Admiten elementos duplicados                            |
| Tipo:              Iterables                                               |
| Pertenencia:       elem in lista                                           |
+----------------------------------------------------------------------------+

+----------------------------------------------------------------------------+
| Tuplas                                                                     |
+----------------------------------------------------------------------------+
| Sintaxis:          (e1, e2, e3)                                            |
| Constructores:     tuple(iterable)                                         |
| Orden:             Ordenados                                               |
| Duplicados:        Admiten elementos duplicados                            |
| Tipo:              Iterables                                               |
| Pertenencia:       elem in tupla                                           |
+----------------------------------------------------------------------------+

+----------------------------------------------------------------------------+
| Conjuntos (Sets)                                                           |
+----------------------------------------------------------------------------+
| Sintaxis:          {e1, e2, e3}                                            |
| Constructores:     set(iterable)                                           |
| Orden:             Sin orden                                               |
| Duplicados:        Elementos únicos                                        |
| Tipo:              Iterables                                               |
| Pertenencia:       elem in set                                             |
+----------------------------------------------------------------------------+

+----------------------------------------------------------------------------+
| Diccionarios                                                               |
+----------------------------------------------------------------------------+
| Sintaxis:          {c1:v1, c2:v2}                                          |
| Constructores:     dict([(c1,v1), (c2,v2)])                                |
| Orden:             Ordenados                                               |
| Duplicados:        Claves únicas | Valores duplicados                      |
| Tipo:              Iterables                                               |
| Pertenencia:       clave in dic.keys()                                     |
|                    valor in dic.values()                                   |
+----------------------------------------------------------------------------+
"""


# ============================================================================
# 3. MÉTODOS DE CADENAS
# ============================================================================

# DIR        - devuelve la lista de atributos válidos del objeto pasado.
# UPPER      - convierte a mayuscula
# LOWER      - convierte a minuscula
# CAPITALIZE - primera en mayuscula

# FIND       - método encuentra la primera aparición del valor especificado, sino devuelve -1
# INDEX      - método encuentra la primera aparición del valor especificado, sino devuelve una excepción

# ISNUMERIC  - si es numerico devuelve true
# ISALPHA    - si es alfa numérico devuelve true

# COUNT      - devuelve el número de ocurrencias de una subcadena en la cadena dada.
# LEN        - cuenta los caracteres de una cadena

# ENDSWITH   - verifica si una cadena termina con
# STARTSWITH - verifica si una cadena comienza con

# REPLACE    - remplaza un valor por otro
# SPLIT      - separa por el parametro dado


# ============================================================================
# 4. MÉTODOS DE LISTAS
# ============================================================================

# LIST    - crea una lista

# LEN     - cuenta la cantidad de elementos de una lista

# APPEND  - agrega un elemento a la lista
# INSERT  - agrega un elemento a la lista en el indice especificado
# EXTEND  - agrega varios elementos a la lista

# POP     - elimina un elemento de una lista, pide indice y devuelve valor
# REMOVE  - remueve un elemento de una lista, pide valor
# CLEAR   - elimina todos los elementos de una lista

# SORT    - ordena una lista de forma ascendente a descendente
# REVERSE - invierte los elementos de una lista


# ============================================================================
# 5. MÉTODOS DE DICCIONARIOS
# ============================================================================

# keys()  -> devuelve las claves
# get()   -> devuelve el valor de una clave
# clear() -> elimina todos los elementos
# pop()   -> elimina un elemento
# items() -> para iterar el dict
