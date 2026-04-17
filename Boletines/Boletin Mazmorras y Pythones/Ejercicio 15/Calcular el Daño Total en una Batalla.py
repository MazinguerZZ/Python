def calcular_damage_final(damages, resistencia):
    if not damages:
        return 0
    else:
        suma = sum(damages)
        damages2 = suma * resistencia
        return int(suma - damages2)
