try:
    fichero = open("quijote.txt", "r")
    print("Posicion: ", fichero.tell()) # tell sirve para decirte en que posicion esta el cursor
    print(fichero.readline())
    print("Posicion: ", fichero.tell())
    # print("Posicion: ", fichero.tell())
    # print(fichero.readline())
    fichero.close()
except:
    print("Error. el fichero no existe")