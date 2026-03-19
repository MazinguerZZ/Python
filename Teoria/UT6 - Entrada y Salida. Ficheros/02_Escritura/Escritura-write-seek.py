try:
    fichero = open("quijote.txt","w+")          # si ponemos r+ el cursor se pone al inicio del fichero y sobreescribe el fichero con lo que pongas,
                                                # si ponemos a+ el cursor se pone al final del fichero
                                                # si ponemos w+ elimina todo y escribe lo nuevo
    fichero.write("\nUna nueva linea")
    print(fichero.tell())
    fichero.seek(0)
    print(fichero.read())
    fichero.close()
except:
    print("Error. el archivo no existe")