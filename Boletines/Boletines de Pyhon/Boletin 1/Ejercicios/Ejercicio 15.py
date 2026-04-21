# 15. Escribir un programa que pida un número al usuario y calcule si es primo o no lo es

numero = int(input("Escribe un número: "))

if numero < 2:
    print("No es primo")
else:
    es_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")