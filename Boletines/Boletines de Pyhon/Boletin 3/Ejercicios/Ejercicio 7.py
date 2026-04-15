# 7. Mejorar el programa anterior para que detecte si se trata de un NIF, un NIE o un CIF de
# empresa y nos comunique, además de si es válido de que tipo es.
# Un CIF es una cadena de 9 caractéres pero en este caso la primera es una letra y las
# otro ocho cifras,
# Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a continuación
# vienen 7 cifras y una letra final.

documento = input("Introduce tu NIF / CIF / NIE: ")

if len(documento) == 9:
    if documento[0:8].isdigit() and documento[8].isalpha():
        print("El NIF es válido.")
    elif documento[0] in "XYZ" and documento[1:8].isdigit() and documento[8].isalpha():
        print("El NIE es válido.")
    elif documento[0].isalpha() and documento[1:].isdigit():
        print("El CIF es válido.")
    else:
        print("El NIF, CIF o NIE no es válido.")
else:
    print("El NIF, CIF, NIE no es válido.")