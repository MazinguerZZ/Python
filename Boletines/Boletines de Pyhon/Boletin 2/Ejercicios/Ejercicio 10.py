# 10. Escribir un programa en python que nos pida elegir entre cuatro destinos turísticos
# (Francia, Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la
# capital de nuestro destino (París, Roma, Santiago de Chile o Tokio)

lugar = input("Elige entre: Francia, Italia, Chile o Japón: ")

if lugar == "Francia":
    print("La capital de Francia es Paris.")
elif lugar == "Italia":
    print("La capital de Italia es Roma.")
elif lugar == "Chile":
    print("La capital de Chile es Santiago de Chile.")
elif lugar == "Japón":
    print("La capital de Japón es Tokyo.")