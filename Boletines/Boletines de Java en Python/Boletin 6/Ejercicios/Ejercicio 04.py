# 4. Validar un número de teléfono con prefijo internacional (empieza por el signo + seguido
# de dos dígitos, luego un espacio y a continuación un número de teléfono.
# Ejemplo +34 912233444
import re

telefono = input("Ingrese el telefono: ")
regex = r"^\+[0-9]{2}\s[0-9]{9}$"
if re.match(regex, telefono):
    print("El telefono es correcto")
else:
    print("El telefono no es correcto")