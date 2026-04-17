def identificar_numeros_magicos(lista):
    lista_nueva = [x for x in lista if x % 3 == 0 and not x % 5 == 0]
    return lista_nueva
