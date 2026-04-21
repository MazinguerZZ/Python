# 2. Validar un número de teléfono
# Ejemplo: 91345566
import re

telefono = input("Ingrese el telefono: ")
regex = r"^[0-9]{9}$"
if re.match(regex, telefono):
    print("El telefono es valido")
else:
    print("El telefono no es valido")
