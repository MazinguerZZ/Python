# 9. Un número de 4 cifras mínimo y 8 cifras máximo
# Ejemplo: 12345
import re

numero = input("Ingrese un numero: ")
regex = r"^[0-9]{4,8}$"

if re.match(regex, numero):
    print("El numero es valido")
else:
    print("El numero no es valido")