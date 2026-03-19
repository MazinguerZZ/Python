# def miFuncion():
#     otroTexto = "Hola mundo cruel"
#     texto = "Hola otra vez mundo"
#     print("Desde dentro de la funcion", texto)
#     return otroTexto
#
#
# texto = "Hola mundo"
# print(miFuncion())
# print("Desde fuera de la funcion", texto)
from itertools import count


# def miFuncion2(texto1, veces):
#      for i in range(0, veces):
#          print(texto1)
#      otroTexto = "Hola otra vez mundo cruel"
#      print(otroTexto)
#
# texto1 = "Hola mundo"
# miFuncion2(texto1, veces=3)
# miFuncion2("Hola mundo cruel", 2)
#
# otroTexto = "Hola mundo cruel"
# miFuncion2("Hola mundo", 3)



# def miFuncion3(t, l, n):
#     t = "Hola mundo cruel"
#     n = 4.4
#     lista[1] = 111  # Las listas si se modifican, los demas no, las listas se pasan por referencia y los demas por valor
#
# texto = "Hola mundo"
# numero = 5.5
# lista = [44,2,13]
# miFuncion3(texto, lista, numero)
# print(texto, "-", numero, "-", lista)


def miFuncion4(l, m):
    l = [8,6,3]
    m = sum(l)/len(l)-1

miFuncion4("La media es: ", m)