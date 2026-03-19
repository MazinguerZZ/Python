class Perro:

    # Asi se declara un constructor

    # def __init__(self, nombre="Bobby"):
    #     self.nombre = nombre


    # __ privada
    # - protegida
    def __init__(self,secreto, secretismo, nombre="Bobby"):
        self.nombre = nombre
        self._secreto = secreto
        self.__secretisimo = secretismo


    # def __init__(self, nombre):
    #     self.nombre = "Bobby"

    # El self sirve para identificar la instancia
    def llamar(self):
        return ("Ey " + self.nombre + " Ven aqui!")

# Llamamos al constructor de la clase perro del primer def
# mascota1 = Perro()
# print(mascota1.llamar())
# mascota2 = Perro("Sultan")
# print(mascota2.llamar())
# mascota1.nombre = "Satan"
# print(mascota1.llamar())


# Llamamos al constructor de la clase perro del segundo def
mascota2 = Perro("Cuchi cuchi", "Cariñito mio", "Sultan")
print(mascota2.llamar())
mascota2._secreto = "Engendro del demonio"
print(mascota2._secreto)
mascota2.__secretisimo = "Elemento inmundo"
mascota2._Perro__secretisimo = "Rata azmilclera"
print(mascota2.__secretisimo)
print(mascota2._Perro__secretisimo)

