import re

patron = r"ola"

if re.match(patron, "olaytsdbs"): # Comprueba si hay una coincidencia al principio de la cadena
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

if re.search(patron, "ytsoladbs"): # Comprueba si hay una coincidencia en cualquier parte de la cadena
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

if re.fullmatch(patron, "olaytsdbs"): # Comprueba si hay una coincidencia exacta en la cadena
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

print(re.fullmatch(patron, "ola"))


# * = 0 o mas
# + = 1 o mas
# ? = 0 o 1

if re.fullmatch(r"[0-9]{3,5}", "1234"): # Entre 0 y 9, minimo 3 y maximo 5
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

if re.fullmatch(r"[0-9]?", "7"): # |1[0-2] significa a partir del 10 hasta el 12
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

# Para comprobar DNI
if re.fullmatch(r"[0-9]{8}[A-Za-z]", "28777666X"): # Entre 0 y 9, minimo 3 y maximo 5
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

# Para comprobar meses
if re.fullmatch(r"[1-9]|12[0-2]", "120"): # |1[0-2] significa a partir del 10 hasta el 12
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

if re.fullmatch(r"[\w+]", "bande545_rola"): # w = valida cualquier palabra
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

if re.fullmatch(r"[^5]", "6"): # ^ = valida cualquier cosa que no sea 5 y que sea un unico caracter
    print("Hay coincidencia")
else:
    print("No hay coincidencia")