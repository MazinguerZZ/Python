import random
pares = 0
impares = 0
lista = []
for i in range(10):
        n = random.randint(1, 1000)
        lista.append(n)
        if(n % 2 == 0):
            pares = pares + 1
        else:
            impares = impares + 1
print("10 numeros entre el 1 y el 1000")
texto = str(lista)
texto = texto[1:-1]
print(texto)
print(lista[0])
lista.sort()
print("He generado ", pares, " numeros pares y ", impares, " numeros impares")
print("El numero mayor ha sido el", lista[9], "y el menor el", lista[0])
