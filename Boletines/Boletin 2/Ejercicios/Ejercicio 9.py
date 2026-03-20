# Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que
# escribamos la palabra FIN (con mayúsculas). Si el usuario introduce una entrada
# inválida (números superiores a 100, otras cadenas de caracteres que no sean FIN, etc.)
# no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá
# su curso. Cuando terminamos (al introducir la palabra FIN, recuerda) mostraremos
# por pantalla el numero de entradas válidas que hemos hecho (sin contar esta última
# que sólo sirve para finalizar el programa)

contador = 0

while True:
    entrada = input("Ingrese un numero: ")
    if entrada == "FIN":
        print("Nº de entradas validas: ", contador)
        break
    elif not entrada.isdigit():
        print("Solo se puede ingrsar FIN")
        continue

    numero = int(entrada)
    if 1 <= numero <= 100:
        contador += 1
    else:
        print("El número tiene que ser menor de 100")
