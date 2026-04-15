# Escribir un programa que sirva como asistente para un juego de rol. Tu programa debería de
# pedir por teclado el número de dados que se van a tirar y el número de caras de estos (4, 6,
# 8, 12, etc.) A continuación debería de hacer la tirada y mostrarla.

import random

tiradas = int(input("Numero de tiradas: "))
dados = tiradas
caras = int(input("Numero de caras: "))

for i in range(dados):
    dados = random.randint(0,caras)
    print(dados)