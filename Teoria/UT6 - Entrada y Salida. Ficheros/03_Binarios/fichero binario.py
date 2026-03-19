import pickle

class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def ver(self):
        print(self.nombre + "(" + str(self.edad) + ")")


p1 = Persona("Pepe",18)
p2 = Persona("Ana",26)
lista = [p1,p2] # Tambien se pueden con listas, tuplas y demas

try:
    fichero = open("persona.bin", "wb")
    pickle.dump(lista, fichero) # Para hacer el fichero en binario, y siempre tiene que se objetos
    # pickle.dump(p2, fichero)
    fichero.close()

    fichero = open("persona.bin", "rb")
    # persona = pickle.load(fichero) # Para cargar el fichero binario y lo lea
    # persona2 = pickle.load(fichero)
    lista = pickle.load(fichero)
    for elemento in lista: # Bucle para recorrer la lista y mostrarla
        print(type(elemento)) # Sirve para ver el tipo del objeto
        elemento.ver()
    # persona.ver() # Lo muestra
    # persona2.ver()
    fichero.close()
except:
    print("Error. el archivo no existe")