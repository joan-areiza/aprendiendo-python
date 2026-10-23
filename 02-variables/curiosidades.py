# Caràcteres validos y no validos
mi_texto_uno = "ADSO"  # VALIDO
mi_texto_dos = 'soy "Tecnòlogo"'  # VALIDO

# mi_texto_uno = "AgroFit" #NO VALIDO
texto_unido = mi_texto_uno + "\n" + mi_texto_dos
print(texto_unido)

texto_unido = mi_texto_uno + "\t" + mi_texto_dos
print(texto_unido)

texto_unido = mi_texto_uno + "\r" + mi_texto_dos
print(texto_unido)
