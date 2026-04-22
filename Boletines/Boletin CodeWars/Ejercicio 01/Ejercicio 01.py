def expression_matter(a, b, c):
    if 1 <= a and b and c <= 10:
        ope1 = a * (b + c)
        ope2 = a * b * c
        ope3 = a + b * c + 1
        ope4 = (a + b) * c
        lista = [ope1, ope2, ope3, ope4]
        maximo = max(lista)
    else:
        print("Numeros mayores de 1 y menores de 10")
    return maximo

print(expression_matter(1, 3, 1))