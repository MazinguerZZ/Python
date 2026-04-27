def shuffle(nums, n):
    lista = []
    for i in range(0, n):
        lista.append(nums[i])
        lista.append(nums[i+n])

    return lista

print(shuffle([2,5,1,3,4,7], 3))
