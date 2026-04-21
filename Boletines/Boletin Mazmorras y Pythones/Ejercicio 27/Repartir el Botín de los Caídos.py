def organizar_botin(objetos):
    mi_dict = {}
    if not objetos:
        return {}
    else:
        for objeto in objetos:
            contar_objeto = objetos.count(objeto)
            mi_dict[objeto] = contar_objeto

    return mi_dict

print(organizar_botin(["oro", "pocion", "oro", "espada", "pocion", "oro"]))
print(organizar_botin(["pocion", "pocion", "pocion"]))
print(organizar_botin([]))