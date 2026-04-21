# Modificar el programa anterior para que nos muestre al final la media aritmética de
# las entradas válidas

lista = []

contador = 0

while True:
    entrada = input("Ingrese un numero: ")
    if entrada == "FIN":
        print("Media aritmetica: ", int(media))
        break
    elif not entrada.isdigit():
        print("Solo se puede ingrsar FIN")
        continue

    numero = int(entrada)
    if 1 <= numero <= 100:
        contador += 1
        lista.append(numero)
        media = sum(lista) / len(lista)
    else:
        print("El número tiene que ser menor de 100")