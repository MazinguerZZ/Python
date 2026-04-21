# 8. Vamos a hacer una implementación del juego del buscaminas y lo primero es preparar el
# tablero. Genera un array de dos dimensiones de 5 filas por 5 columnas. El tablero
# tendrá 5 minas que se colocaran de forma aleatoria en cinco posiciones del array. Las
# minas se representarán con un 1 y las posiciones sin mina con un 0. Al final dibuja el
# tablero de esta forma:
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 1 0 1
# 0 0 0 0 0
# 1 1 0 0 0
import random

tablero = []

for i in range(5):
    fila = [0] * 5
    tablero.append(fila)

minas = 0

while minas < 5:
    fila = random.randint(0, 4)
    columna = random.randint(0, 4)

    if tablero[fila][columna] == 0:
        tablero[fila][columna] = 1
        minas += 1

for fila in tablero:
    for valor in fila:
        print(valor, end=" ")
    print()
