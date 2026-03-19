class Perro:
    numPerros = 0
    def __init__(self, nombre="Bobby"):
        self.nombre = nombre
        Perro.numPerros+=1
    def llamar(self):
        return "Ey " + self.nombre + " Ven aqui!"

    def sobrecargada(self, atributo):
        if isinstance(atributo, int):
            print("Estoy trabajando con un entero")
        elif isinstance(atributo, float):
            print("Estoy trabajando con un float")
        elif isinstance(atributo, str):
            print("Estoy trabajando con un string")
        elif isinstance(atributo, list):
            print("Estoy trabajando con una lista")
        else:
            print("Estoy trabajando con otra cosa")

    def sobrecargada2(self, *atributo):
        if (len(atributo)==1):
            print("Recibo un parametro")
        elif(len(atributo)==2):
            print("Recibo 2 parametros")
        else:
            print("Recibo 3 paramentros")

mascota1 = Perro("Sultan")
mascota2 = Perro()
mascota3 = Perro("Tobby")

mascota3.sobrecargada(3)
mascota3.sobrecargada(3.5)
mascota3.sobrecargada("Hola")
mascota3.sobrecargada([1,2,3])

mascota2.sobrecargada2(1,2)
mascota2.sobrecargada2(1)
mascota2.sobrecargada2(1, "Hola", 3.5, [1,3])

