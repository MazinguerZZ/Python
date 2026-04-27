def mergeAlternately(word1, word2):
    lista = []
    indice = 0
    while indice < len(word1) or indice < len(word2):
        if indice < len(word1):
            lista.append(word1[indice])
        if indice < len(word2):
            lista.append(word2[indice])

        indice += 1
    return "".join(lista)

print(mergeAlternately("abc", "def"))