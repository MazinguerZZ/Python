def decodificar_manuscrito(texto):
    lista = []
    texto = texto.replace(" ", "")
    for name in texto:
        name = ord(name)
        lista.append(name)
    return lista

