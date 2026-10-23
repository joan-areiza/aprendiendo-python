
def SumDig(num1):
    resultado = sum(int(n) for n in str(num1))
    return resultado

num = True 
print("\nEl ingreso de numeros terminara cunado digite 0")
print("\n-----------------------------------------------")

while num != 0:
    num = int(input("\nDigite un numero: "))
    dig = SumDig(num)
    if num != 0:
        print(f"La suma de los digitos de {num} es de: {dig} ")
print("Numero cero detectado ... Finalizar")

