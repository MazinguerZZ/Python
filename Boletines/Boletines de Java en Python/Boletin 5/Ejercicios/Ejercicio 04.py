# 4. Escribir un programa que nos pida una cadena por teclado y luego cuente cuantas
# palabras hay en ella con cuatro o más vocales diferentes. Por ejemplo, si introducimos
# la frase “Crisis constitucional por culpa del murcielago guineoecuatorial” Nos debería
# de decir que 3. Tendrías que tener en cuenta que las vocales pueden ir en mayúsculas
# o no y son la misma letra. Presupón que ninguna vocal va acentuada de ninguna
# forma.

frase = input("Ingrese una frase: ")

palabras = frase.split()
contador = 0

for palabra in palabras:
    palabra = palabra.lower()
    vocales_encontradas = []

    for letra in palabra:
        if letra in "aeiou" and letra not in vocales_encontradas:
            vocales_encontradas.append(letra)

    if len(vocales_encontradas) >= 4:
        contador += 1

print("Cantidad de palabras con 4 o más vocales diferentes:", contador)