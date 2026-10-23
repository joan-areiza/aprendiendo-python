def titulo(text):
    words = text.split(" ")
    mayus = [palabra.title() for palabra in words]
    cadena = " ".join(mayus)
    return cadena

cant = int(input("\nDigite cuantas cadenas va a ingresar: "))
print("\n--------------------------------------------------")

for i in range(1, cant + 1):
    text = str(input(f"\nDigite la cadena Nº{i}: "))
    textMayus = titulo(text)
    print(f"La cadena resultante es: {textMayus}")
print("\n--------------------------------------------------")
