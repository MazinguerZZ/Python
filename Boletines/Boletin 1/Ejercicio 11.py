# Modificar el programa anterior para que tu programa tire dos dados de forma continuada
# hasta que el número que salga en ambos sea el mismo. En ese momento debería de parar la
# ejecución e informarnos de cuantas tiradas ha tenido que hacer para llegar a ese resultado
import random

dado1 = 1
dado2 = 6
contador = 0

while dado1 != dado2:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(dado1, "-", dado2)
    contador+=1
print("Se ha repetido: ", contador ,"veces.")