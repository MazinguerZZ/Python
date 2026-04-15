# 8. Escribe un programa que sume por un lado las cifras pares y por otro las impares de
# un número y nos muestre ambos resultados. Por ejemplo, si el número en cuestión es
# el 128 nos debería e decir que la suma de las cifras pares es 9 y la de las impares 2

numero = input("Ingrese un numero: ")
resultado = 0
resultado2 = 0

for num in numero:
    if int(num) % 2 == 0:
        resultado += int(num)
    else:
        resultado2 += int(num)
print("La suma de las cifras pares del numero", numero, "es: ", resultado)
print("La suma de las cifras impares del numero", numero, "es: ", resultado2)