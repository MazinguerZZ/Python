def es_palindromo(texto):
    alReves = texto[::-1].lower().replace(" ","")
    texto = texto.lower().replace(" ","")

    if texto == alReves:
        return True
    else:
        return False
