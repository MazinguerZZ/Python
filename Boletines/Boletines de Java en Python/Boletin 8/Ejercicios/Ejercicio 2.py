# 2. Escribe un programa que pida al usuario una contraseña y compruebe que cumple las
# siguientes condiciones:
# a. Debe tener al menos 8 caracteres y no más de 20.
# b. Debe tener al menos una letra mayúscula y una minúscula.
# c. Debe de tener al menos un número
# c. Debe tener un símbolo de entre los siguientes: _, -, !, ?, *
# Si la contraseña no es válida, se pide de nuevo, y así sucesivamente hasta que sea correcta.
# Una vez que es correcta se pide al usuario que la introduzca de nuevo, si coincide se informa
# al usuario y se termina el proceso. Si no coincide se vuelve a empezar el proceso.

esValida = False

while not esValida:
    password = input("Introduce la contraseña: ")
    password2 = input("Introduce de nuevo la contraseña: ")
    tieneMayuscula = False
    tieneMinuscula = False
    tieneNumero = False
    tieneCaracter = False
    if len(password) >= 8 <= 20:
        for caracter in password:
            if caracter.isupper():
                tieneMayuscula = True
                esValida = False
            elif caracter.islower():
                tieneMinuscula = True
                esValida = False
            elif caracter.isdigit():
                tieneNumero = True
                esValida = False
            elif caracter in "_-!?*":
                tieneCaracter = True
                esValida = False

        if tieneMayuscula == True and tieneMinuscula == True and tieneNumero == True and tieneCaracter == True:
            print("Contraseña valida")
            esValida = True
        else:
            print("Contraseña invalida")
    else:
        input("Contraseña invalida, escribela de nuevo: ")
        esValida = False