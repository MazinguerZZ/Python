def find_uniq(arr):
    return min(set(arr), key=arr.count) # cuenta cuántas veces aparece cada número y devuelve el que menos aparece


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 3, 10, 3, 3, 3 ]))