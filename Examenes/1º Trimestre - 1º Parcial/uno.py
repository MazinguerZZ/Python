import random
maximo = int(input("Escribe un numero: "))
while(maximo < 10):
    print("No puedo generar 5 numeros aleatorios pares diferentes entre el 1 y el " , maximo)
    maximo = int(input("Escribe un numero: "))
print("5 numeros pares aleatorios y diferentes comprendidos entre el 1 y el", str(maximo))
candidatos=[]
for i in range(2,maximo+1,2):
    candidatos.append(i)
resultado = random.sample(candidatos, 5)
for i in resultado:
    print(i)