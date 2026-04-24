def digitize(n):
    lista = []
    n = str(n)
    for i in n:
        i = int(i)
        lista.append(i)
    return lista[::-1]

print(digitize(35231))
print(digitize(0))