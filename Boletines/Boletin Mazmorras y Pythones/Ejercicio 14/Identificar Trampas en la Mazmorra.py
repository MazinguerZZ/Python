def identificar_trampas(lista):
    lista_negativa = []
    for num in lista:
        if num < 0:
            lista_negativa.append(num)
    return lista_negativa
