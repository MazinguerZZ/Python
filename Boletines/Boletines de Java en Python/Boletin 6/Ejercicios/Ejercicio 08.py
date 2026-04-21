# 8. Un IBAN bancario de España. Las dos letras iniciales siempre tienen que ser ES
# Ejemplo: ES61 1234 3456 42 0456323532
import re

iban = input("Ingrese el IBAN: ")
regex = "^ES[0-9]{2} [0-9]{4} [0-9]{4} [0-9]{2} [0-9]{10}$"
if re.match(regex, iban):
    print("El IBAN es valido")
else:
    print("El IBAN es invalido")