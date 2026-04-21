def prueba_elemental(elementos_disponibles, combinacion_requerida):
    for elemento in set(combinacion_requerida):
        if combinacion_requerida.count(elemento) > elementos_disponibles.count(elemento):
            return False
    return True