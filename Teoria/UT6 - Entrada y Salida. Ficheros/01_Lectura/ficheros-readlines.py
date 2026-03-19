try:
    fichero = open("quijote.txt", "rt")

    lineas = fichero.readlines()
    for i in range(len(lineas)): # Forma para quitar el ultimo caracter que sea /n y no otro
        if lineas[i][-1] == "\n":
            lineas[i] = lineas[i][:-1]
    print(lineas)

    # for l in lineas: # Te lo da con saltos de linea
    #     print(l[:-1]) # Suprime el ultimo /n y caracter
    # fichero.close()
except:
    print("Error. el fichero no existe")