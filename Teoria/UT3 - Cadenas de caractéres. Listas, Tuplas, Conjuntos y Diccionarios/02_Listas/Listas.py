# # 2 formas de crear las listas
# lista = []
# lista2 = list()
#
# # lista con datos
lista3 = [2, 5, 6, 7, 8, 12, 7]
#
# lista4 = [34, "Pepe", False, 7567.45, [1, 2, 3]] # Es valido, en java no
#
# print(lista4)
#
# # Ejemplo 1
# for elemento in lista4:
#     print(elemento)
#
# # Ejemplo 2
# for posicion in range(0, len(lista4)):
#     print(posicion, "-", lista4[posicion])
#
#
# # Añadir elementos a una lista
# lista4.append("Nuevo elemento")
# print(lista4)
#
# # Añadir elementos con el operador de suma +
# lista5 = lista3 + [23, 45]
# print(lista5)
#
# lista6 = lista5 + lista4
# print(lista6)
#
#
# # Extrae el elemento que indicamos
# print(lista3)
# lista3.pop(1)
# print(lista3)
#
# # Por su valor, solo elimina el primer elemento que encuentre, oseaq, el primer 7, el siguiente no
# lista3.remove(7)
# print(lista3)


# El metodo sort para ordenar mientras todos los elementos sean homogeneos, mezclados da error, solo funciona numeros con numeros o letras con letras
print(lista3)
lista3.sort(reverse=True) # reverse sirve para ordenar descendientemente
print(lista3)


