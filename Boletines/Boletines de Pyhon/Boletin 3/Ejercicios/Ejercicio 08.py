# 8. Las matrículas españolas constan de un número de cuatro dígitos y tres letras
# cualesquiera en mayúsculas a excepción de la Ñ y la Q. Escribe un programa en Python
# que detecte si una matrícula introducida por el usuario es válida o no.

matricula = input("Introduce la matrícula a comprobar: ")

if len(matricula) == 7 and matricula[0:4].isdigit() and matricula[4:].isalpha():
    valida = True
    for letra in matricula[4:]:
        if letra in "ÑQ":
            valida = False
    if valida:
        print("La matrícula es válida.")
    else:
        print("La matrícula no es válida.")
else:
    print("La matrícula no es válida")