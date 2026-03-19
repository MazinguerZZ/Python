# read = lo lee entero
# readline = lee el fichero entero pero lo devuelve en una lista, y si pongo readline(2), solo lee los 2 primeros caracteres y el cursor se situa en el siguiente caracter
# readlines = lee una linea completa del fichero, y situa el cursor en la siguiente linea


try:
    fichero = open("quijote.txt", "rt")
    texto = fichero.read()
    print(texto)
    fichero.close()
except:
    print("Error. el fichero no existe")