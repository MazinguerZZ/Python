# 7. Validar una tarjeta de crédito: cuatro grupos de cuatro números cada uno separados por
# un espacio. A continuación un espacio y la fecha de caducidad en formato MM/YY. El
# mes tiene que ser válido (entre 01 y 12)
# Ejemplo: 1234 5678 9012 3456 03/25
import re

tarjeta = input("Ingrese la tarjeta de credito: ")
regex = "^[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4} (0[1-9]|1[0-2])/[0-9]{2}$"

if re.match(regex, tarjeta):
    print("La tarjeta de credito es valida")
else:
    print("La tarjeta de credito es invalida")