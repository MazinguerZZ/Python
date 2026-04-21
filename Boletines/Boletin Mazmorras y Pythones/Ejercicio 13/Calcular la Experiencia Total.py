def calcular_experiencia_total(experiencia):
    if not experiencia:
        return 0
    else:
        experiencia = sum(experiencia)
    return experiencia
