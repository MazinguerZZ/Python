# print("Inicio del programa")
# try:
#     x = 45/0
#     print(x)
# except:
#     print("Excepcion")
# finally:
#     print("El finally no es obligatorio y se ejecuta haya o no haya excepcion")
# print("Fin del programa")


# print("Inicio del programa")
# try:
#     denominador = int(input("Introduce el denominador: "))
#     x = 45/denominador
#     print(x)
# except ZeroDivisionError:
#     print("No se puede dividir por cero")
# except ValueError:
#     print("No puedo convertirlo a entero")
# except:
#     print("Excepcion no reconocida")
# finally:
#     print("El finally no es obligatorio y se ejecuta haya o no haya excepcion")
# print("Fin del programa")


print("Inicio del programa")
try:    # Es obligatorio
    denominador = int(input("Introduce el denominador: "))
    x = 45/denominador
    print(x)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("No puedo convertirlo a entero")
except: # Es obligatorio y seria el except general
    print("Excepcion no reconocida")
else:   # Es opcional
    print("No ha ocurrido ninguna excepcion")
finally:    # Es opcional
    print("El finally no es obligatorio y se ejecuta haya o no haya excepcion")
print("Fin del programa")

try:
    num1 = int(input("Mete un numero "))
    num2 = int(input("Mete un numero "))
    if(0 <= num1 and 0 <= num2):
        print(num1 + num2)
    else:
        raise Exception("Añade un numero que sea mayor a 0")
except Exception as e: # ALIAS as nombre alias
    print("ERROR", e)
