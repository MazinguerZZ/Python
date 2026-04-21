def encontrar_objeto_legendario(objetos):
    if not objetos:
        return ""
    return max(objetos, key=lambda x: x[1])

print(encontrar_objeto_legendario([["Espada", 3], ["Escudo", 5], ["Armadura", 4]]))