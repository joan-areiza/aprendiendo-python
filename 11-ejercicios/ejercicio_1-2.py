#Solicitar al usuario que ingrese su direcciòn email. Imprimir un mensaje
#O no, valièndose de una funciòn para decidirlo. Una direcciòn se considera
#"@".

def email():
    correo = input("Digite el correo electronico")
    if correo.count("@gmail.com") or correo.count("@outlook.com"):
        print("correo valido")
    else:
        print("correo no valido, falta el caracter @")
email()