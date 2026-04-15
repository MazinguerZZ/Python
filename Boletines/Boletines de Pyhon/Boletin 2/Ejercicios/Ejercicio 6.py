# 6. Escribir un programa en python que pida una entrada por teclado hasta que escribamos
# la palabra FIN (con mayúsculas). En ese caso terminamos y mostramos por pantalla el
# numero de entradas válidas que hemos hecho (sin contar esta última que sólo sirve para
# finalizar el programa)

esFin = True
contador = 0

while esFin:
    texto = input("Introduce cualquier cosa: ")
    if texto != "FIN":
        esFin = True
        contador += 1
    else:
        esFin = False
        break

print("Has introducido", contador, "entradas validas.")

