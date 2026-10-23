# Programaciòn orientada a objetos (POO - OOP)
# Definir una clase {molde para crear mas objetos de ese mismo tipo}
# {vehiculo} con caracteristicas similares

class Vehiculo:
    # Atributos o propiedades {variables}
    # Caracteristicas del vehìculo
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos, son acciones que hace el objeto {vehiculos} -> {funciones}
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definiciòn de clase
# Crear objetos / Instanciar la clase
vehiculo = Vehiculo()

print("VEHICULO 1: ")
vehiculo.setColor("amarillo")
vehiculo.setModelo("Murcielago")

print(vehiculo.marca, vehiculo.getModelo(), vehiculo.getColor())
print("Velocidad actual: ", vehiculo.getVelocidad())

vehiculo.acelerar()
vehiculo.acelerar()
vehiculo.acelerar()
vehiculo.acelerar()

vehiculo.frenar()

print("Velocidad nueva: ", vehiculo.getVelocidad())

print("----------------------------------------")

# Crear mas objetos
vehiculo2 = Vehiculo()

vehiculo2.setColor("Verde")
vehiculo2.setModelo("Gallardo")

print("VEHICULO 2: ")

print(vehiculo2.marca, vehiculo2.getModelo(), vehiculo2.getColor())
