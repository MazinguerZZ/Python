# El valor puede ser el que tu quieras, una lista, tupla o hasta otro diccionario

d1 = dict(Sara = [1,2,3], Pepe = 55, Luis = 44, Manolo = 33, Eva = 66, Ines = 55)
print(d1)

# Si la clave no existe, te la añade, si existe, no hace nada, solo comprueba
d1.setdefault("Antonio", 56)
print(d1)
