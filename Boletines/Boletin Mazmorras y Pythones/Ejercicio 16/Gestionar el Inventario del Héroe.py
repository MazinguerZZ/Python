def actualizar_inventario(inventario, objeto, capacidad, accion):
    if len(inventario) < capacidad and accion == "agregar":
        inventario.append(objeto)
        return inventario
    elif len(inventario) <= capacidad and accion == "eliminar" and objeto in inventario:
        inventario.remove(objeto)
        return inventario
    else:
        return inventario

print(actualizar_inventario(["espada", "escudo"], "poción", 3, "agregar"))
print(actualizar_inventario(["espada", "escudo", "poción"], "arco", 3, "agregar"))
print(actualizar_inventario(["espada", "poción"], "escudo", 3, "eliminar"))
print(actualizar_inventario(["espada", "escudo", "arco"], "arco", 3, "eliminar"))