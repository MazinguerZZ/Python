fibonacci = [0,1]
numero = int(input("¿Cuántos números de la sucesión de Fibonacci quieres? "))
if numero == 1:
    fibonacci.pop()
elif numero==0:
    fibonacci = []
else:
    for _ in range(2,numero):
        nuevo = fibonacci[-1]+fibonacci[-2]
        fibonacci.append(nuevo)
print(fibonacci)
