# 9. Escribir un programa que nos pida por teclado primero una cadena y luego un
# carácter. A continuación debe de imprimirnos cuantas veces aparece dicho carácter y
# en las posiciones de la cadena donde lo hace. Por ejemplo, si nuestra cadena es Hola
# Mundo y el carácter la o nos debería de decir algo así:
# La o aparece en 2 ocasiones
# Las posiciones en las que aparece son: 1,9

texto = input("Ingrese un frase: ")
letra = input("Ingrese una letra: ")
contador = 0
posiciones = ""

for i, posicion in enumerate(texto):
    if posicion == letra:
        contador += 1
        posiciones = posiciones + str(i) + ","
print("La", letra, "aparece en", contador, "ocasiones.")
print("Las posiciones en las que aparece son: ", posiciones.rstrip(","))
