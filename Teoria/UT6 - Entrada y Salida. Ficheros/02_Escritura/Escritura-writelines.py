# write = escribe normal
# writelines = escribe en lista

try:
    fichero = open("quijote.txt", "at")
    lista = ["Jorge", "Eva", "Ana", "Pepa"]
    fichero.writelines(lista)
    fichero.close()



except:
    print("Error. el fichero no existe")