# Ejercicio 2 – RA3 (3 puntos)
# Jinx necesita tu ayuda para contactar con Ekko sin que la policía de Piltover
# se entere. Para ello necesita previamente cifrar sus mensajes, por lo que te
# pide que escribas un programa en Python automatizando el proceso.
# El programa de cifrado en cuestión debe pedir al usuario que escriba una
# palabra y una clave numérica por teclado. Tras esto, escribirá la palabra del
# revés y cambiará todas sus vocales por el valor de la clave. (2 puntos)
# Para mejorar aún más el infalible sistema de cifrado que se le ha ocurrido, Jinx
# te pide separar la palabra cifrada en dos, a partir de la letra en la posición
# indicada como clave. Por último, quiere pasar la palabra a mayúsculas si la
# clave es par o a minúsculas si la clave es impar. (1 punto)

palabra = input("Introduce una palabra: ")
clave = int(input("Introduce una clave numérica: "))

letra = (palabra[::-1].replace("a", f"{clave}").replace("A", f"{clave}").
         replace("e", f"{clave}").replace("E", f"{clave}").
         replace("i", f"{clave}").replace("I", f"{clave}").
         replace("o", f"{clave}").replace("O", f"{clave}").
         replace("u", f"{clave}").replace("U", f"{clave}"))
print(letra, end="")


parte1 = letra[:clave]
parte2 = letra[clave:]

palabra_final = parte1 + parte2

if clave % 2 == 0:
    palabra_final = palabra_final.upper()
else:
    palabra_final = palabra_final.lower()

print(palabra_final)

