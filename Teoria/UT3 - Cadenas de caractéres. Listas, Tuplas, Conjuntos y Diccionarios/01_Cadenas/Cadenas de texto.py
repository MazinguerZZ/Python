texto = "Hola mundo"
print(texto.upper()) # Te convierte la cadena a mayúscula
print(texto.lower()) # Te convierte la cadena a minúscula
print(texto.swapcase()) # Te convierte las mayúsculas en minúsculas y las minúsculas en mayúsculas

print(texto.find("o")) # Te muestra la primera posicion donde aparece el caracter
print(texto.count("o")) # Te muestra el numero de veces que aparece el caracter
print(texto.replace("do", "x")) # Te reemplaza los caracteres
print(texto[2:].replace("o", "x")) # El [2:] desde la posicion que quieres que empiece, y siempre empienza en 0
print(texto.replace("o", "x", 1)) # El count es para que solo te sustituya el numero de veces que digas

# print(len(texto)) # Para contar los caracteres que hay
#

#
# cadenaNumerica = str(3456.5) # Te permite convertir de tipo numerico(Integer) a tipo texto(String)
# print(cadenaNumerica)

# texto[2] = "x"  # No se pueden modificar cadenas de texto

#for c in texto:
#    print(c)

# for i in range (0, len(texto)):   para que te salga el el numero a la par de la letra
#    print(i, "-", texto[i])


