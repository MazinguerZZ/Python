# Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
# espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
# que ha encontrado y suprimido.

texto = input("Introduce tu texto: ")

contador = 0

for letra in texto:
    if letra == " ":
        contador += 1
        print(texto.replace(" ", ""))
        print("Espacios eliminados: ", contador)


