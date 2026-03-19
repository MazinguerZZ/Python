texto = input("Escribe un texto: ")
textoFinal = ""
espaciosSuprimidos = 0
vocalesSuprimidas = 0
listaVocales = ["a","e","i","o","u","A","E","I","O","U"]
for caracter in texto:
    if caracter == " ":
        espaciosSuprimidos = espaciosSuprimidos + 1
    elif caracter in listaVocales:
        vocalesSuprimidas = vocalesSuprimidas + 1
    else:
        textoFinal = textoFinal + caracter

print("Sin vocales ni espacios: ", textoFinal)
print("Vocales suprimidas: ", vocalesSuprimidas)
print("Espacios suprimidos: ", espaciosSuprimidos)