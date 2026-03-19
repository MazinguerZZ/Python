class Perro:
    # Atributos de clase fuera de los metodos
    numPerros = 0
    def __init__(self, nombre="Bobby"):
        self.nombre = nombre
        Perro.numPerros+=1
    def llamar(self):
        return ("Ey " + self.nombre + " Ven aqui!")

    def cuantosPerros(self):
        return (Perro.numPerros)

mascota1 = Perro("Sultan")
mascota2 = Perro("Bobby")
mascota3 = Perro("Tobby")

# Da igual al que llames que te daran siempre el mismo resultado
print(mascota2.cuantosPerros())
print(mascota1.cuantosPerros())
print(mascota3.cuantosPerros())

# No da error pero cambia el valor
Perro.numPerros = 10
print(mascota2.cuantosPerros())

