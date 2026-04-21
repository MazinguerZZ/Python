# 2. Escribir una función en python que genere de forma consecutiva tiradas de dados aleatorios
# entre el 1 y el 6 ambos incluidos y los muestre en pantalla finalizando la ejecución cuando el
# valor de todos los dados es el mismo. Al finalizar debe de decir cuantas veces ha tenido que
# lanzar los dados para alcanzar ese valor.

# EJEMPLO DE EJECUCIÓN:

#       INVOCACIÓN DE LA FUNCIÓN                RESULTADO EN LA CONSOLA
#       tiradadosmultiple(3)                    2 – 5 - 1
#                                               4 – 1 - 4
#                                               4 – 6 - 6
#                                               3 – 3 - 3
#                                               He tenido que lanzar los dados 4 veces para
#                                               que todos sean iguales
import random

def tiradadosmultiple(valor):
    coincide = True
    contador = 0

    while coincide:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        dado3 = random.randint(1, 6)

        if valor == dado1 == dado2 == dado3:
            coincide = False
            print(f"{dado1} - {dado2} - {dado3}")
            print(f"He tenido que lanzar los dados {contador + 1} veces para que todos sean iguales")
        else:
            print(f"{dado1} - {dado2} - {dado3}")
            contador += 1

tiradadosmultiple(4)
