# Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
# Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
# nuestro destino (París, Roma, Santiago de Chile o Tokio)

ciudad = input("Ingrese un ciudad (Francia, Italia, Chile o Japon): ")

match ciudad:
    case "Francia":
        print("La capital de Francia es Paris")
    case "Italia":
        print("La capital de Italia es Roma")
    case "Chile":
        print("La capital de Chile es Santiago")
    case "Japon":
        print("La capital de Japon es Tokyo")