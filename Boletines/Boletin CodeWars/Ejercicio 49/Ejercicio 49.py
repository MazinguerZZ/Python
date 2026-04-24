def friend(x):
    lista = []
    for i in x:
        if len(i) == 4:
            lista.append(i)
    return lista


print(friend(["Ryan", "Kieran", "Mark",]))
print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]))