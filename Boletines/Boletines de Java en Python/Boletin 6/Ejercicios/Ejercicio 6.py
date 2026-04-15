# 6. Una clave con el siguiente formato XX00-xxX-00 donde las X deben de ser letras
# mayúsculas, las x letras minúsculas y los 0 dígitos.
# Ejemplo: AB12-xyZ-75
import re

clave = input("Ingrese la clave: ")
regex = r"^[A-Z]{2}[0-9]{2}-[a-z]{2}[A-Z]-[0-9]{2}$"

if re.match(regex, clave):
    print("El clave es valida")
else:
    print("El clave es invalida")