# 1. Vamos a hacer una pequeña calculadora. Solicita dos números al usuario y luego que
# escriba la operación que quiere hacer (S para suma, R para resta, M para multiplicar y D
# para dividir). Realiza la operación con un switch.
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
operacion = input("Seleccione una operacion: S para suma, R para resta, "
                  "M para multiplicar y D para dividir: ")

match operacion:
    case "S":
        print("Solución de la suma: ", numero1 + numero2)
    case "R":
        print("Solución de la resta: ", numero1 - numero2)
    case "M":
        print("Solución de la multiplicación: ", numero1 * numero2)
    case "D":
        print("Solución de la división: ", numero1 / numero2)
