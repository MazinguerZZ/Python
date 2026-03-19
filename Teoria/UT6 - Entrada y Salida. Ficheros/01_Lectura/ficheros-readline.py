try:
    fichero = open("quijote.txt", "rt")
    linea = fichero.readline(5) # lee de 5 en 5 caracteres
    while linea!="":
        print(linea)
        linea = fichero.readline(5)
    fichero.close()
except:
    print("Error. el fichero no existe")