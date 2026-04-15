# 2. Idem al anterior pero pidiéndonos apellidos de personas
apellido1 = input("Dame el primer apellido: ")
apellido2 = input("Dame el segundo apellido: ")
apellido3 = input("Dame el tercer apellido: ")

if apellido1 > apellido2:
    apellido1, apellido2 = apellido2, apellido1

if apellido1 > apellido3:
    apellido1, apellido3 = apellido3, apellido1

if apellido2 > apellido3:
    apellido2, apellido3 = apellido3, apellido2

print(apellido1, "<", apellido2, "<", apellido3)