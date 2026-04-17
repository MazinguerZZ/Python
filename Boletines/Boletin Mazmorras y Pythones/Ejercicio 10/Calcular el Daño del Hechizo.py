def calcular_damage_hechizo(damage_base, multiplicador):
    if multiplicador < 1:
        return damage_base
    else:
        return int(damage_base * multiplicador)