# 3. Validar un número de teléfono móvil (debe de empezar por 6, 7 u 8)
# Ejemplo: 655776655
import re

telefono = input("Ingrese el telefono: ")
regex = r"^[6-8]{1}[0-9]{8}$"

if re.match(regex, telefono):
    print("El telefono es valido")
else:
    print("El telefono no es valido")