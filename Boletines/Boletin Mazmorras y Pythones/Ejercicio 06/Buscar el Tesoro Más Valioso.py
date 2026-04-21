def buscar_tesoro(lista):
    if not lista:
        return -1
    else:
        return max(lista)