def calcular_vida(vida, damage):
    if vida < damage:
        return 0
    else:
        return vida - damage