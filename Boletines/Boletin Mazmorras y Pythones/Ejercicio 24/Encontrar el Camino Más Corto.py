def camino_mas_corto(distancias):
    if not distancias:
        return -1
    else:
        minimo = min(distancias)

    return minimo

print(camino_mas_corto([10, 5, 15, 8]))