# 1

# Pedimos al usuario un número entero
numero = int(input("Introduce un número para calcular su factorial: "))

# Inicializamos el resultado en 1 (ya que el factorial de 0 es 1)
factorial = 1

# Usamos un bucle para multiplicar desde el número hasta 1
for i in range(1, numero + 1):
    factorial *= i

# Mostramos el resultado
print(f"El factorial de {numero} es {factorial}")

# 2 

# Pedimos al usuario cuántos números de Fibonacci quiere
cantidad = int(input("¿Cuántos números de Fibonacci quieres ver?: "))

# Inicializamos la lista con los dos primeros números
fibonacci = [0, 1]

# Generamos la sucesión hasta alcanzar la cantidad deseada
while len(fibonacci) < cantidad:
    siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente)

# Mostramos la lista completa
print("Sucesión de Fibonacci:", ",".join(map(str, fibonacci[:cantidad])))

# 3 

# Pedimos al usuario un número límite
limite = int(input("Introduce un número límite para la sucesión de Fibonacci: "))

# Inicializamos la lista con los dos primeros números
fibonacci = [0, 1]

# Generamos la sucesión mientras el siguiente número sea menor o igual al límite
while True:
    siguiente = fibonacci[-1] + fibonacci[-2]
    if siguiente > limite:
        break
    fibonacci.append(siguiente)

# Mostramos los números que cumplen la condición
print("Números de Fibonacci menores o iguales a", limite, ":", ",".join(map(str, fibonacci)))

# 4 

numero = str(input("Ejercicio 4: Introduce un número: "))
count = 0

for i in range(0, len(numero)):
    if numero[i].isdigit():
            count+=1
print(count)

# 5

numero = input("Ejercicio 5: Introduce un número: ")

principio = 0
fin = len(numero) - 1
es_palindromo = True

while principio < fin:
    if numero[principio] != numero[fin]:
        es_palindromo = False
        break
    principio += 1
    fin -= 1

if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")


# 9

cadena = input("Ejercicio 9: Introduce una cadena: ").lower()
caracter = input("Ejercicio 9: Introduce un caracter: ").lower()
count = 0

print("Las posiciones en las que aparece son:", end=" ")

for i in range(len(cadena)):
    if cadena[i] == caracter:
        count += 1
        print(i, end=" ")

print("\nLa", caracter, "aparece en", count, "ocasiones.")


# 10

frase = str(input("Ejercicio 10: Introduce una frase: "))
digitos = ""

for i in range(len(frase)):
    if frase[i].isdigit():
        digitos += frase[i]
print(digitos)

# 11

frase = input("Ejercicio 11: Introduce una frase: ")
palabras = frase.split()
fraseGuiones = ""

for palabra in palabras:
    for letra in palabra:
        if letra.isalpha():
            fraseGuiones += letra + "-"
    fraseGuiones = fraseGuiones.rstrip("-")  # Quita el guión final de cada palabra
    fraseGuiones += " "

print(fraseGuiones.rstrip())

# 12

# 13

numero = int(input("Ejercicio 13: Introduce un numero: "))
caracter = str(input("Ejercicio 13: Introduce un caracter: "))

for i in range(numero):
    for a in range (numero):
        print(caracter, end=" ")
    print()
        
