# 5. Escribir un programa en python que guarde en un diccionario los precios de las
# frutas de la siguiente tabla:
# Fruta Precio (€/Kg)
# Aguacate 4.35
# Mandarina 2.60
# Kiwi 3.75
# Naranja 1.80
# NOTA: El diccionario debes de crearlo en el código del programa con los datos listados en
# la tabla
# Tú programa debe de preguntar al usuario por una fruta y un número de kilos y mostrar por
# pantalla el precio de ese número de kilos de fruta con dos decimales. El número de kilos
# debe de admitir decimales. Si la fruta no está en el diccionario debe mostrar un mensaje
# informando de ello. Captura las posibles excepciones.
# El programa finalizará cuando se escriba la palabra fin (de forma insensible a mayúsculas
# y/o minúsuculas)

lista_frutas = {"Aguacate": 4.35, "Mandarina": 2.60, "Kiwi": 3.75, "Naranja": 1.80}


def mostrar_fruta():
    if fruta in lista_frutas:
        for frutas in lista_frutas:
            if fruta == frutas:
                precio_kilos = round(lista_frutas[frutas] * kilos, 2)
                print(frutas, ": ",precio_kilos, "€")
    else:
        print("La fruta que quieres comprar no esta en stock")

try:
    while True:
        fruta = input("Ingrese la fruta que quieres comprar: ")
        if fruta.lower() == "fin" or fruta.upper() == "FIN":
            break
        else:
            kilos = float(input("Ingrese el número de kilos a comprar: "))
            mostrar_fruta()
except Exception as e:
    print("Error: ", e)