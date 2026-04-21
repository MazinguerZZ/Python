def crear_mapa(filas, columnas):
    matriz = []

    for i in range(filas):
        filas = []
        for j in range(columnas):
            filas.append(".")
        matriz.append(filas)
    return matriz

print(crear_mapa(3, 4))
print(crear_mapa(2, 2))
print(crear_mapa(1, 5))