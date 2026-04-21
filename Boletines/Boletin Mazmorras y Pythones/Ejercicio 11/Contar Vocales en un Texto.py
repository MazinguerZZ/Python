def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
            contador += 1

    return contador
