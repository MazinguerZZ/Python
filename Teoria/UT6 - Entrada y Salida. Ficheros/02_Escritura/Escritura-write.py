# write = escribe normal
# writelines = escribe en lista

try:
    # fichero = open("quijote.txt", "wt")
    # fichero.write("En un lugar de la Mancha\n")
    # fichero.write("de cuyo nombre no quiero acordarme\n")
    # fichero.write("no ha mucho que vivia\n")
    # fichero.write("un hidalgo caballero...")
    # fichero.close()

    with open("fichero.txt", "at") as fichero: # abre un fichero y cuando acabe el bloque lo cierra automaticamente
        fichero.write(1) # Tiene que se en modo texto -> "1"
        fichero.write("Dos\n")
        fichero.write(3.55)
except:
    print("Error. el fichero no existe")