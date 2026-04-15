# Escribe un programa que pida un número por teclado y escriba todos sus divisores
# separados por comas (y evitando poner una coma al final).

numero = int(input("Ingrese un numero: "))

texto = ""

for i in range(1, numero + 1):
    if numero % i == 0:
        texto += str(i) + ", "

texto = texto.rstrip(", ")  # rstrip sirve para eliminar el caracter final

print(f"Divisores del número {numero}: {texto}")