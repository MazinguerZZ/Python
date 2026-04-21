# 1. Crear un programa o una función que reciba un diccionario con los datos de los clientes de una tienda
# y su edad y los muestre por consola ordenados por nombre de pila. El diccionario, ya creado en el
# código de tu programa, tendrá esta forma
# clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto,
# Francisco": 44, "Cotón, Carmelo": 56 }
# Y la salida por consola así:
# Carmelo Cotón (56)
# Francisco Rupto (44)
# José Chuletón (35)
# Rubén Tosidad (27)

clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }

def obtener_nombre(elemento):
    partes = elemento.split(", ")
    return partes[1]


def lectura():
    for elemento in sorted(clientes, key=obtener_nombre):
        partes = elemento.split(", ")
        print(partes[1], partes[0], "(",clientes[elemento], ")")
lectura()