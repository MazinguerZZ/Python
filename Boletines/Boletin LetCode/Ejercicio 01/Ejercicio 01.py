def getConcatenation(nums):
    lista = list(nums)
    ans = []
    for i in lista:
        ans.append(i)
    for j in lista:
        ans.append(j)
    return ans

print(getConcatenation([1,2,1]))