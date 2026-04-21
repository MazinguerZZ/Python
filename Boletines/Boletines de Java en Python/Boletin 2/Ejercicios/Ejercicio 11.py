# Modificar el programa anterior para que, además, nos diga al final cual han sido el
# número mayor y el menor que has introducido

lista = []

contador = 0

while True:
    entrada = input("Ingrese un numero: ")
    if entrada == "FIN":
        print("Media aritmetica: ", int(media))
        print("Mayor numero: ", max(lista))
        print("Menor numero: ", min(lista))
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