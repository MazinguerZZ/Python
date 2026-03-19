class Empleado:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

# Getter de java, para recuperar el valor
    @property
    def edad(self):
        return(self.__edad)

    @property
    def nombre(self):
        return(self.__nombre)

# Setter de java, para modificar el valor
    @edad.setter
    def edad(self, nuevaEdad):
        self.__edad = nuevaEdad

    @edad.setter
    def edad(self, nuevoNombre):
        self.__nombre= nuevoNombre

emp1 = Empleado("Jose Maria", 57)
print(emp1.edad)
print(emp1.nombre)
emp1.edad = 58      # No se puede cambiar el valor con getter pero si con setter
print(emp1.edad)
