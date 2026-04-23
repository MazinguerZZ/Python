def count_char_occurrences(strng, char):
    contador = 0
    for i in strng:
        if i == char:
            contador += 1
    return contador

print(count_char_occurrences("missippi", "i"))