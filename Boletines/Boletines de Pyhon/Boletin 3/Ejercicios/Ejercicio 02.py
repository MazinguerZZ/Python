# 2. Escribir un programa que pida al usuario que escriba una cadena de texto y la imprima
# escrita al reves (es decir, si el usuario escribe Hola Mundo el programa debería de
# escribir odnuM aloH)

texto = input("Introduce una frase: ")

cadena_invertida = texto[::-1]
print(cadena_invertida)