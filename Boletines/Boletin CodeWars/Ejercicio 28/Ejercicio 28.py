def first(seq, n=1):
    lista = []
    for i in range(0, n):
        if i < len(seq):
            lista.append(seq[i])
        else:
            return seq[::1]

    return lista


print(first(['a', 'b', 'c', 'd', 'e', ]))