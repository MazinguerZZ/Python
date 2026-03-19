def saludo (nombre, mensage="Hola", despedida="Hasta la vista"):
    print(mensage, nombre, despedida)

saludo("Jose Maria", despedida="Nos vemos pronto")
saludo("Jose Maria", "Bienvenido")

def argumentosVariables(nombre, *titulo):
    for titulo in titulo:
        print(titulo, end=" ")
    print(nombre)

argumentosVariables("Jose Maria", "Sr")
argumentosVariables("Jose Maria", "Excelentisimo", "Ilustrismo", "Sr", "Don")

def muestraDatos(nombre, edad):
    print("Nombre:", nombre, "- Edad:", edad)

muestraDatos("Jose Maria", 57)
datos = ["Pedro", 32]
muestraDatos(*datos)

def devuelveTresEnteros():
    return 14, 17, 25

num1, num2, num3 = devuelveTresEnteros()
print(num1, num2, num3, sep=" - ")


def devolvertupla(pin : int) -> tuple:
    pass