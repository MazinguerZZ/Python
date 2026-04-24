def maps(a):
    lista = []
    for i in a:
        nuevo = i * 2
        lista.append(nuevo)
    return lista


print(maps([1,2,3]))
print(maps([0,1,2,3,4,5,6,7,8,9]))