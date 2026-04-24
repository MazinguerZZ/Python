def wave(people):
    lista = []
    for i in range(len(people)):
        if people[i] != " ":
            palabra = people[:i] + people[i].upper() + people[i+1:]
            lista.append(palabra)
    return lista

print(wave("hello"))