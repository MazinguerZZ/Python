# 3. Por último, crea ahora una función que sume un año a la edad de un cliente. La
# llamada sería así:
# cumpleCliente(clientes, “José”, “Chuletón”)
# Si el cliente existe debería de sumar un año a su edad. Si no existe debería de
# informar de ello por consola y no hacer nada

clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }

def obtener_nombre(elemento):
    partes = elemento.split(", ")
    return partes[1]


def lectura():
    for elemento in sorted(clientes, key=obtener_nombre):
        partes = elemento.split(", ")
        print(partes[1], partes[0], "(",clientes[elemento], ")")

def escritura(cliente, apellido, nombre ,edad):
    clave = apellido + ", " + nombre
    if clave in clientes:
        sobrescribir = input("El cliente ya existe, ¿quieres que se sobrescriba?: ")
        if sobrescribir == "Si":
            clientes[clave] = edad
    else:
        clientes[clave] = edad


escritura(clientes , "Pineros", "Marcos", 25)
escritura(clientes , "Pineros", "Marcos", 18)
lectura()
