def count_by(x, n):
    lista = []
    for i in range(1, n + 1):
        i = i * x
        lista.append(i)
    return lista

print(count_by(1, 5))
print(count_by(2, 5))
