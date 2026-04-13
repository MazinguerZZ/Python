# 1. Validar un código postal de Madrid. Cinco números, los dos
# primeros siempre son el 28
# Ejemplo: 28032
import re

cod_postal = input("Ingrese el codigo postal: ")
regex = r"^28[0-9]{3}$"
if re.match(regex, cod_postal):
    print("El codigo postal es valido")
else:
    print("El codigo postal es invalido")