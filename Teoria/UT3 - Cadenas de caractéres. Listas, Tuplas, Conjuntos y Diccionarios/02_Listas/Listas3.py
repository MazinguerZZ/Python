# lista = ["Ana", "Pedro", "Luis"]
#
# # Metodos para recorrer listas
# for nombre in lista:
#     print(nombre)
#
# for i in range(len(lista)):
#     print(i, "-", lista[i])
#
# for i, nombre in enumerate(lista):
#     print(i, "-", nombre)
#


# Para hacer una copia de la lista original
numero1 = [7]
numero2 = numero1.copy()
numero2[0] = numero2[0] * 2
print(numero2)
print(numero1)

def miFuncion(lista):
    pass
miFuncion(numero1.copy())