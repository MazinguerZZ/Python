# Escribe un programa que valide si un NIF español introducido por teclado es correcto.
# La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
# ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
# escrita en mayúsculas o minúsculas.

import re

nif = input("Ingrese nif: ")

regex = re.compile("^[0-9]{8}[A-Z]$")

if re.match(regex, nif):
    print("El nif es valido")
else:
    print("El nif no es valido")