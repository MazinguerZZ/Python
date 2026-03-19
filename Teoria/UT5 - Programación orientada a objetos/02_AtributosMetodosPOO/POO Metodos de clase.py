class Perro:
    numPerros = 0
    def __init__(self, nombre="Bobby"):
        self.nombre = nombre
        Perro.numPerros+=1
    def llamar(self):
        return "Ey " + self.nombre + " Ven aqui!"


    @classmethod
#    @staticmethod
    def cuantosPerros(cls):
        return cls.numPerros



mascota1 = Perro("Sultan")
mascota2 = Perro()
mascota3 = Perro("Tobby")

print(Perro.cuantosPerros())