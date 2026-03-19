import re

try:
    fichero = open("movistar.txt", "rt")
    fichero2 = open("movistar2.txt", "wt")
    texto = fichero.read()
    regex = r"^[6-8]\[0-9]{8}$"
    if re.match(regex, texto):
        fichero2.write(texto)

    fichero.close()
except:
    print("Error. el fichero no existe")