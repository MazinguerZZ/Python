# 5. Validar dos palabras de cualquier tamaño separadas por un único espacio en blanco.
# Las palabras no pueden contener números y deben de empezar ambas por una letra
# mayúscula.
# Ejemplo: Hola Mundo
import re

palabras = input("Ingrese las palabras: ")
regex = "^[A-Z][a-z]+ [A-Z][a-z]+$"

if re.match(regex, palabras):
    print("La frase es correcta")
else:
    print("La frase es incorrecta")