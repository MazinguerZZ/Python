# 6. Escribe un programa en Python que valide si un NIF español es correcto. La longitud
# exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de ser números
# comprendidos entre el 0 y el 9 y el último una letra, no importa que esté en mayúsculas
# o minúsculas. Usa para ello las funciones isdigit e isalpha:

nif = input("Introduce tu NIF: ")

if len(nif) == 9:
    if nif[0::7].isdigit() and nif[::8]:
        print("El NIF es válido.")
    else:
        print("El NIF no es válido.")
else:
    print("El NIF no es válido.")
