def cuadrado(x):
    return x**2

print(cuadrado(5))

# Funcion de arriba con lambda
cuadradoLambda = lambda x: x**2
print(cuadradoLambda(5))

media =lambda *lista: sum(lista)/len(lista)
print(media(3,5,1,7))
print(media(5,5,1))

cuadradoMayorQue10 = lambda x: True if x**2 >=10 else False
print(cuadradoMayorQue10(3))
print(cuadradoMayorQue10(4))