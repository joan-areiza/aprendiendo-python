cantantes = ['2pac','Drake','Bad bunny','Julio Iglesias']
numeros = [1,2,5,8,3,4]

#Ordenar una lista
#print(numeros)
numeros.sort() #Ordena los datos de la lista
#print(numeros)

#Añadir elementos a la lista
cantantes.append("Don Omar")
cantantes.insert(1, "Tito Nieves")
#print(cantantes)

#Eliminar elementos de la lista
cantantes.pop(1)
cantantes.remove('Don Omar')
#print(cantantes)

#Dar la vuelta a una lista
#print(numeros)
numeros.reverse()
#print(numeros)

#Buscar dentro de una lista
#print('Drake' in cantantes)

#Contar elementos de la lista
#print(cantantes)
#print(len(cantantes))

#Cuantas veces aparece un elemento
numeros.append(8)
#print(numeros.count(8))

#Unir listas
cantantes.extend(numeros)
print(cantantes)