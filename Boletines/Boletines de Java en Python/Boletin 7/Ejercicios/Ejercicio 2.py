# 2. Incluye operaciones adicionales (raiz cuadrada, cuadrado, cubo, por ejemplo)
import math

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
operacion = input("Seleccione una operacion: S para suma, R para resta, "
                  "M para multiplicar, D para dividir, RC para la raiz cuadrada, "
                  "C para elevar al cuadrado, CU para elevar al cubo: ")
operacion_extra = numero1 + numero2

match operacion:
    case "S":
        print("Solución de la suma: ", numero1 + numero2)
    case "R":
        print("Solución de la resta: ", numero1 - numero2)
    case "M":
        print("Solución de la multiplicación: ", numero1 * numero2)
    case "D":
        print("Solución de la división: ", numero1 / numero2)
    case "RC":
        print("Solución de la raiz cuadrada: ", math.sqrt(operacion_extra))
    case "C":
        print("Solución elevado al cuadrado: ", operacion_extra ** 2)
    case "CU":
        print("Solución elevado al cubo: ", operacion_extra ** 3)
