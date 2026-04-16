# 2. Idem, pero que ponga los divisores uno detrás de otro separados por comas en lugar de
# uno debajo de otro

numero = int(input("Introduce un número: "))
print(f"Los divisores de {numero} son: ")
primero = True

for i in range(1, numero):
    if numero % i == 0:
        if not primero:
            print(",", end=" ")

        print(i, end="")
        primero = False