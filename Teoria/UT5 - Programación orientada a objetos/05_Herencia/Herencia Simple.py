class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"

    def getNombre(self):
        return self.nombre

# "ClaseB" hereda de "ClaseA"
class ClaseB(ClaseA):
    def __init__(self):
        self.nombre = "Clase B"


objetoa = ClaseA()
objetob = ClaseB()
print(objetoa.getNombre())
print(objetob.getNombre())

