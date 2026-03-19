from time import clock_settime


class Empleado:
    def __init__(self, nombre, apellidos, edad):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad

# Getter de java, para recuperar el valor
    @property
    def edad(self):
        return self.__edad

    @property
    def nombre(self):
        return self.__nombre

# Setter de java, para modificar el valor
    @edad.setter
    def edad(self, nuevaEdad):
        self.__edad = nuevaEdad




emp1 = Empleado("Jose Maria", "Morales Vazquez",57)
# print(emp1.edad)
# print(emp1.nombre)
emp1.edad = 58      # No se puede cambiar el valor con getter pero si con setter
# print(emp1.edad)





class Cuenta:
    def __init__(self, titular, saldo):
        self.__titular = []
        self.__titular.append(titular)
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

# "__str__" para concatenar
    def __str__(self):
       return str(self.__saldo) + ", " + str(self.__titular)

# "__add__" para sumar objetos, eso si, tienes que declarar en el contructor la lista y poner el append para añadir a la lista
    def __add__(self, cuenta):
        self.__saldo = self.__saldo + cuenta.__saldo
        self.__titular = self.__titular + cuenta.__titular
        return self

c1 = Cuenta("Jose Maria Morales", 1234.66)
c2 = Cuenta("Maria Rodriguez", 345.78)
print(c1.titular)
print(c1.saldo)

print(str(c1))

c1 = c1 + c2
print(c1.titular)
print(c1.saldo)