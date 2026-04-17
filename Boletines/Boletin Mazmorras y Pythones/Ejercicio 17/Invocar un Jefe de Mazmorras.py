def invocar_jefe(dificultad, jugadores):
    diccionario = {'jefe': 'Dragón de Fuego', 'recompensa': 'Espada Legendaria'}
    jugador = len(jugadores)
    if dificultad > 4 and jugador > 2:
        return diccionario
    else:
        return "No hay suficientes jugadores o la dificultad es demasiado baja"
