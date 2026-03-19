# Para eliminar un elemento random del diccionario

import random

d1 = dict(Sara = 33, Pepe = 55, Luis = 44, Manolo = 33, Eva = 66, Ines = 55)
print(d1)


def eliminarAlAzar(d1):
    claves = list()
    for elemento in d1:
        claves.append(elemento)
    borrar = random.choice(claves)
    print("Elemento a borrar: ",borrar)
    d1.pop(borrar)
    print(d1)

eliminarAlAzar(d1)

# Si sales de la funcion, los cambios se siguen guardando
print(d1)


def eliminarAlAzar2(d1):
    claves = list(d1.keys())
    for elemento in d1:
        claves.append(elemento)
    borrar = random.choice(claves)
    print("Elemento a borrar: ",borrar)
    d1.pop(borrar)
    print(d1)

eliminarAlAzar2(d1)


texto = str(d1)
print("En texto", texto)