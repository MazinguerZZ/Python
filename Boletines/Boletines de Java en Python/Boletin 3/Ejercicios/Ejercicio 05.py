# Escribir un programa que pida por teclado una cadena de texto y la imprima escrita al
# reves (es decir, si el usuario escribe Hola Mundo el programa debería de escribir
# odnuM aloH)

texto = input("Introduce tu texto: ")

invertido = texto[::-1]
print(invertido)