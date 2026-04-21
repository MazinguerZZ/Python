# 2. Añade una función que sirva para añadir nombres al diccionario. La llamada a la
# función sería así:
# nuevoCliente(clientes, “Felipe”, “Lotas”, 76)
# Tu función debería de añadir el nuevo cliente al diccionario con el formato correcto. Si
# este cliente ya existe debería de mostrar en consola un mensaje advirtiéndolo y preguntando
# si se quiere sobreescribir la edad o no

clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }

def obtener_nombre(elemento):
    partes = elemento.split(", ")
    return partes[1]


def lectura():
    for elemento in sorted(clientes, key=obtener_nombre):
        partes = elemento.split(", ")
        print(partes[1], partes[0], "(",clientes[elemento], ")")

def escritura(nombre, edad):
    clientes[nombre] = edad

escritura("Pineros, Marcos", 18)
lectura()