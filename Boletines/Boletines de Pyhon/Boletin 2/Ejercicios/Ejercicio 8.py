# 8. Escribir un programa en python que pida una contraseña por teclado (dos veces) y si no
# coinciden nos las vuelva a pedir hasta que lo hagan

password = input("Dime tu contraseña: ")

esCorrecta = True

while esCorrecta:
    password2 = input("Repite tu contraseña de nuevo: ")
    esCorrecta = False
    if password != password2:
        esCorrecta = True
        print("La contraseña es incorrecta. Repite de nuevo.")
    else:
        print("La contraseña es correcta.")
        break