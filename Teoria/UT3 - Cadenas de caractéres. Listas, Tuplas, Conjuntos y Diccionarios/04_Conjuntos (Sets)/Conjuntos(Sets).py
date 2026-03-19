from runpy import run_path

profesPrimero = {"Ana", "Juan Carlos", "Sancho", "Natalia"}
print(profesPrimero)
profesSegundo = set(["Agustin", "Ana", "Natalia", "Javier", "Jose Maria"])
print(profesSegundo)

# Condicion
if "Juan Carlos" in profesPrimero:
    print("Juan Carlos da clases en primero")
if "Javier" in profesSegundo:
    print("Javier no da calses en primero")

# Recorridos
for elemento in profesPrimero:
    print(elemento)

# Contar elementos
print(len(profesPrimero))

for i in range(0,len(profesPrimero)): # Si funciona
    #print(profesPrimero[i]) # No funciona
    print("Hola") # Si funciona

# Añadir elemento a los conjuntos y no admiten duplicados
profesPrimero.add("Jose Maria")
print(profesPrimero)

# Eliminar un elemento
profesPrimero.remove("Jose Maria")
print(profesPrimero)


# Alternativa de remove, discard no provoca excepcion si el elemento no esta, remove si
profesPrimero.discard("Jose Maria")
print(profesPrimero)


# Para coger el primer elemento del conjunto
profe = profesPrimero.pop()
print(profe)
print(profesPrimero)


# Para vaciar el conjunto
#profesPrimero.clear()
#print(profesPrimero)


# Conversiones
# De lista a conjunto
conjunto1 = set([1,2,3,4,5,1,5,6,4,2,3])
print(conjunto1)
# De tupla a conjunto
conjunto2 = set((1,2,3,4,5,1,5,6,4,2,3))
print(conjunto2)
# De texto a conjunto
conjunto3 = set("Hola mundo cruel")
print(conjunto3)
# De conjunto a lista
lista = list(profesPrimero)
print(lista)
# De conjunto a tupla
tupla = tuple(profesPrimero)
print(tupla)
# De conjunto a texto
texto = str(profesPrimero)
print(texto)


# Operaciones que obtienes un conjunto nuevo sin modificar el original
# Union |
print(profesPrimero | profesSegundo)
print(profesPrimero.union(profesSegundo))

# Interseccion &
print(profesPrimero & profesSegundo)
print(profesPrimero.intersection(profesSegundo))

# Diferencia -
print(profesPrimero - profesSegundo)
print(profesPrimero.difference(profesSegundo))

# Exclusive or ^
print(profesPrimero ^ profesSegundo)
print(profesPrimero.symmetric_difference(profesSegundo))
