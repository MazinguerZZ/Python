# Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado por el usuario (se introducirá por teclado)
numero = int(input("Dame un numero: "))
for i in range(1,6):
    print(i*numero)