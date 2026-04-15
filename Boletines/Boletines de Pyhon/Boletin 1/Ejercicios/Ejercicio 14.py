# 14. Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que
# sólo se detenga cuando salga el 666
import random

num_random = 0

while num_random != 666:
    num_random = random.randint(1, 1001)
    print(num_random)