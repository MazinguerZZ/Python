# Ejercicio 3 – RA3 (3,5 puntos)
# El héroe más poderoso de todos, Saitama, no es precisamente un genio. No
# sabe si ha suspendido o no el módulo de Fundamentos de Programación al
# que se ha apuntado, por lo que te ha pedido ayuda.
# Para ello tienes que escribir un programa en Python que pida al usuario
# enteros por teclado, hasta introducir la cadena END, calculando la media de
# los valores introducidos y mostrándola por pantalla. (2,5 puntos)
# Pero Saitama no consigue utilizar correctamente el programa. Para mejorarlo
# se necesitaría hacer que compruebe que el usuario introduzca solo valores
# entre 0 y 10, ignorando el resto de casos y mostrando un aviso de error por
# pantalla. (1 punto)

esEnd = True
lista = []

while esEnd:
    try:
        numero = input("Introduce tu nota: ")
        if numero == "END":
            esEnd = False
            print(f"La media es: {round(sum(lista) / len(lista), 2)}")
        elif 0 <= int(numero) <= 10:
            num = int(numero)
            lista.append(num)
        else:
            print("El numero tiene que estar entre 0 y 10")
            esEnd = True
    except Exception as e:
        print("Error: ", e)
