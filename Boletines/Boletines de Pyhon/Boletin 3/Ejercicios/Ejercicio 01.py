# 1. Escribir un programa en python que pida al usuario una cadena de texto y la escriba en
# sin espacios en blanco (si los hubiera). Además, nos debe de decir el número de
# espacios que ha encontrado y suprimido.

texto = input("Introduce una cadena de texto: ")
contador = 0
sin_Espacios = ""

for i in texto:
    if i == " ":
        contador += 1
sin_Espacios = texto.replace(" ", "")
print("Frase sin espacios: ", sin_Espacios)
print("Espacios eliminados: ", contador)