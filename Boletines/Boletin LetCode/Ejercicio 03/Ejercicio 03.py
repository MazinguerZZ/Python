def findMaxConsecutiveOnes(nums):
    lista = list(nums)
    contador = 0
    maximo = 0
    for i in lista:
        if i == 1:
            contador += 1
            maximo = max(maximo, contador)
        else:
            contador = 0
    return maximo

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))

