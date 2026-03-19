try:
    fichero = open("quijote.txt", "r")
    print("Posicion: ", fichero.tell()) # tell sirve para decirte en que posicion esta el cursor
    print(fichero.readline())
    fichero.seek(0, 2)  # seek sirve para devolverte a la posicion que tu quieras

    print("Posicion: ", fichero.tell())
    # print("Posicion: ", fichero.tell())
    # print(fichero.readline())
    fichero.close()
except:
    print("Error. el fichero no existe")
