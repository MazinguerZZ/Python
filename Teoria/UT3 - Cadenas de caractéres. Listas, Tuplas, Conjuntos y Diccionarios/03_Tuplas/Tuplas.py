tupla = (1,2,3,4,5)
print(tupla)
tupla2 = ("Maria","Hola","Pepe")
tupla3 = (23, "Adrian Alvarez", False, (1,2,3), 44.5, [1,2,3])
print(tupla3)
tupla4 = ()
print(tupla4)
tupla5 = ("Sevilla",)  # Para tener formato de dupla poner coma, solo sirve en duplas de 1 elemento
print(tupla5)

# Para recorrer duplas
for elemento in tupla5:
    print(elemento)

for i in range(0,len(tupla5)):
    print(i, "-", tupla5[i])

# Para trasformar a tuplas(tuple), a listas(list) o a texto(str)
lista = list(tupla2)
print(lista)
texto = str(tupla2)
print(texto)
tupla6 = tuple([1,2,3,4,5])
print(tupla6)
tupla7 = tuple("Hola mundo")
print(tupla7)

# Tambien sirve para crer tuplas
tupla8 = "Pepe", "Juan",tupla6, "Ana"
print(tupla8)

# No se puede añadir elementos a tuplas
# tupla8[1] = "Rocio"

# La unica forma de modificar tuplas
print(tupla3[5])
tupla3[5][1] = 4
print(tupla3)

# Para buscar un elemeto
if 4 in tupla:
    print("El 4 esta en mi tupla")

if 33 not in tupla:
    print("El 33 no esta en mi tupla")

# Asignacion multiple, tambien se peude en listas
profesor = ("Jose María", "Morales", 57, False, True)
nombre, apellidos, edad, alumno, profesor = profesor
print(apellidos, edad)