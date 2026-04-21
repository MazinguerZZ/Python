def descifrar_codigo(codigo_cifrado):
    numeros = codigo_cifrado.split(",")
    mensaje = ""

    for num in numeros:
        letra = chr(int(num) + 64)
        mensaje += letra
    return mensaje


print(descifrar_codigo("8, 5, 12, 12, 15"))