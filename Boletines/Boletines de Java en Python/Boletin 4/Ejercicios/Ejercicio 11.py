# 11. Escribir un programa que nos pida una frase por teclado y luego nos la imprima
# separando todos los caracteres de sus palabras (excepto los espacios) con un guión.
# Por ejemplo, si la frase introducida es “esto es una prueba” la salida del programa
# debería de ser “e-s-t-o e-s u-n-a p-r-u-e-b-a”

frase = input("Ingrese una frase: ")

for letra in range(len(frase)):
    if letra != " ":
        print(letra, end="-")
    else:
        print(" ")