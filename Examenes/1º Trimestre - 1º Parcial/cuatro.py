fraccion = input("Escribe tu fraccion: ")
lista = list(fraccion)

if lista.count("/") == 1:
    posicion = fraccion.find("/")
    if posicion == 0 or posicion == len(fraccion)-1:
        print("La barra no puede estar ni en la primaera posicion ni en la ultima")
    else:
        numerador = fraccion[:posicion]
        denominador = fraccion[posicion+1:]
        if numerador.isdigit() == False or denominador.isdigit() == False:
            print("El numerador y/o el denominador no son numeros enteros")
        else:
            numerador = int(numerador)
            denominador = int(denominador)
            if denominador == 0:
                print("No puedo dividir entre cero")
            else:
                print("El valor de tu fraccion es ", round(numerador/denominador, 3))
else:
    print("Una fraccion debe tener una y solo una /")