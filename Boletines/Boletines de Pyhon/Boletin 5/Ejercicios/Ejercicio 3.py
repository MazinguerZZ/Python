# 3. Escribir un programa que vaya llenando una lista con números hasta que introduzcamos
# uno negativo. En ese momento debe de parar y mostrarnos la lista ordenada
# ascendente y descendentemente.
# NOTA: Si introducimos algo que no sea un número debería de advertirnos, no
# introducirlo en la lista pero contunuar la introducción de datos

esNegativo = True
lista = []


while esNegativo:
    try:
        numero = int(input("Introduce un número: "))

        if numero < 0:
            print("Lista ordenada de manera ascendente:", sorted(lista))
            print("Lista ordenada de manera descendente:", sorted(lista, reverse=True))
            esNegativo = False
        else:
            lista.append(numero)

    except Exception:
        print("Error valor incorrecto")
        esNegativo = True