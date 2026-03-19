import random

#Primera forma de resolver
dado1 = 1
dado2 = 6
contador = 0

while dado1 != dado2:
   dado1 = random.randint(1, 6)
   dado2 = random.randint(1, 6)
   print(dado1 , "-" , dado2)
   contador+=1
print("Nuemero de intentos: ", contador)


#Segunda forma de resolver
dado1 = 1
dado2 = 1
contador = 0
iguales = False

while iguales == False:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 == dado2:
        iguales = True
    print(dado1 , "-" , dado2)
    contador+=1
print("Nuemero de intentos: ", contador)
