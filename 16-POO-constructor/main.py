from vehiculo import Vehiculo

carro = Vehiculo("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Vehiculo("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Vehiculo("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Vehiculo("Rojo", "Mercedes", "Clase A", 350, 400, 4)


print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar Tipado
carro3 = "Aleatorio"
if type(carro3) == Vehiculo:
    print("Es un objeto correcto!")
else:
    print("No es un objeto correcto!")

#Visibilidad
print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())