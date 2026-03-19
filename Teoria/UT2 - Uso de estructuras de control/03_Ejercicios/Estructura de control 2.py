import random

lista4 = ["Jorge", "Pepe", "Ana", "Manoli", "Roberto", "Pilar"]
print(random.choice(lista4)) # Coge un elemento aleatorio
print(random.sample(lista4, 3)) # Coge el numero de elementos que digamos y sin repeticion
random.shuffle(lista4) # Ordena aleatoriamente
print(lista4)

cadena = "a"
if cadena.isalpha(): # Me devuelve true cuando todo el texto son letras
    print("Son letras")
else:
    print("No son letras")


cadena = "12.3"
if cadena.isdigit(): # Me devuelve true cuando todo el texto son numeros enteros
    print("Son numeros")
else:
    print("No son numeros")

# Tambien existen estos
    # isdecimal = Sirve para saber si esta en un formato decimal
    # isnumeric = Sirve para saber si todos los caracteres de una cadena son números.
    # isalnum = Verifica si todos los caracteres son alfanuméricos (letras y/o números, sin espacios ni símbolos).
    # isspace = Verifica si la cadena contiene solo espacios en blanco, tabulaciones (\t), saltos de línea (\n), etc.
    # isprintable = Comprueba si todos los caracteres son imprimibles, es decir, si se pueden mostrar en pantalla (no son caracteres de control como \n, \t, etc.).