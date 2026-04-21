# 3. Realiza un juego que consiste en acertar un numero que el ordenador elige de forma
# aleatoria entre 1 y 50. Para ello se leen por teclado una serie de números, para los que
# se indica ”mayor”' o “menor”, según sea mayor o menor respecto al numero secreto. El
# proceso termina cuando se acierta o cuando se superan el número máximo de intentos
# establecidos en 3. Si lo prefieres, puedes parametrizar la dificultad del juego
# estableciendo dos variables para el número máximo (50) o el número de intentos (3)
import random

max_num = 50
max_intentos = 3
contador = 0
hasAcertado = True
num_random = random.randint(1, max_num)

while hasAcertado:
    if contador != max_intentos:
        numero = int(input("Ingrese un número: "))
        if num_random < numero:
            print("El número es menor.")
            contador += 1
        elif num_random > numero:
            print("El número es mayor.")
            contador += 1
        elif num_random == numero:
            print("Has acertado.")
            hasAcertado = False
    else:
        print("Ya no te quedan mas intentos.")
        hasAcertado = False