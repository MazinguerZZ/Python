class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 55

    def cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

class ClaseB(ClaseA):
    def __init__(self):
# Super invoca a la funcion que le digamos, en este caso invocamos el constructor de la clase padre que en este caso es "Clase A", o
# tambien le decir que esta llamando a la clase padre
        super().__init__()
        self.subclase = "Clase B"


    def incrementaCodigo(self):
        self.codigo +=1

objetoa = ClaseA()
objetob = ClaseB()
print(objetoa.nombre)
print(objetob.nombre)
print(objetob.subclase)