# Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
# informe del número de intentos inválidos

contador = 0

while True:
    contraseña = input("Introduce tu contraseña: ")
    contraseña2 = input("Introduce tu contraseña de nuevo: ")
    if contraseña == contraseña2:
        print("Correcto")
        print(f"Numero de intentos invalidos: {contador}")
        break
    else:
        print("Incorrecto")
        contador += 1
        continue