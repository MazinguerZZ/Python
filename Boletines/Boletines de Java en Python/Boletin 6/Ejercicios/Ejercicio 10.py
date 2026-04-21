# 10. Una dirección IP pública de clase C. Cuatro bytes en formato decimal separados por un
# punto. Los dos primeros tienen que ser siempre 192.168.
# Ejemplo: 192.168.30.30
import re

ip = input("Ingrese la direccion IP: ")
regex = "^192.168.[0-9]{1,3}.[0-9]{1,3}$"

if re.match(regex, ip):
    print("La direccion IP es valida")
else:
    print("La direccion IP no es valida")