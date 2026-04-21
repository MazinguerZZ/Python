# Escribir un programa que pida una contraseña por teclado (dos veces) y si no
# coinciden nos lo vuelva a pedir hasta que lo hagan

while True:
    contraseña = input("Introduce tu contraseña: ")
    contraseña2 = input("Introduce tu contraseña de nuevo: ")
    if contraseña == contraseña2:
        print("Correcto")
        break
    else:
        print("Incorrecto")
        continue

