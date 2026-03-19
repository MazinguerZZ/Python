opcion = input("P para jugar, C para configurar o X para salir")
match opcion:
    case "P" | "p" | "J" | "j": # | para tener varias opciones
        print("Has elegido jugar")
    case "C":
        print("Has elegido configurar")
    case "X":
        print("Has elegido salir. Hasta la proxima")
    case _: #_ para poner opcion por defecto
        print("Opcion no valida")
print("Fin del menu")