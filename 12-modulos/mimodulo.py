def holaMundo(nombre):
    return f"¿Hola como estas?, {nombre}"

# Solicitar nùmeros al usuario hasta que ingrese el cero.
# Por cada uno, mostrar la suma de sus digitos
# (Utilizando una funciòn que realice dicha suma)

def suma():
    numero = int(input('Digite un numero: '))
    while numero != 0:
        lista = list(str(numero))
        sumas = [int(num) for num in lista]
        print(sum(sumas))
        numero = int(input('Digite un numero: '))
suma()