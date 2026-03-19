class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 55

    def queSoy(self):
        print("Soy clase A")

class ClaseB:
    def __init__(self):
        self.nombre = "Clase B"

    def queSoy(self):
        print("Soy clase B")

class ClaseC(ClaseA, ClaseB):
    def queSoy(self):
        ClaseA.queSoy(self)
        super().queSoy()
        ClaseB.queSoy(self)
        print("Y ademas soy clase C")

class ClaseD(ClaseB, ClaseA):
    pass

objetoa = ClaseA()
objetob = ClaseB()
objetoc = ClaseC()
objetoc.queSoy()
# objetod = ClaseD()

# print(objetoa.nombre)
# print(objetob.nombre)
# print(objetoc.codigo)
# print(objetod.nombre)
