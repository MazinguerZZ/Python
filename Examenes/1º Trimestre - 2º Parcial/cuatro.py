red = input("Dame una direccion ip: ")
bytes = red.split(".")
correcta = True

if len(bytes) != 4:
    correcta = False
else:
    for byte in bytes:
        if byte.isdigit() == False:
            correcta = False
        elif int(byte) < 0 or int(byte) > 255:
            correcta = False

if correcta == False:
    print("Direccion no valida")
else:
    if int(bytes[0]) < 128:
        red = red + "/8"
        print(red)
    elif int(bytes[0]) < 192:
        red = red + "/16"
        print(red)
    elif int(bytes[0]) < 224:
        red = red + "/24"
        print(red)
    else:
        print("Direccion reservada")