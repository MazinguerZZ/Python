# ArrayList = List = LinkedList
# HashMap = Diccionarios = TreeMap
# HashSet = Set = TreeSet


# Diccionario = {clave:valor}
# No puedes tener 2 elementos duplicados, y si lo hay, el ultimo sobreescribe al primero
dicc1 = {"Nombre": "Sara", "Edad": 57, "Solterx": True, "Edad": 33}
print(dicc1)

#Para crear un diccionario vacio con dict(), el dict() es como si fuera el constructor
dicc2 = dict()
dicc2["Nuevo"] = "Hola"
print(dicc2)


dicc3 = dict(Primero = "Uno", Tercero = "Tres")
dicc3["Segundo"] = "Dos"
print(dicc3)

# Para crear diccionarios vacios
dicc4 = {}
dicc4["Edad"] = 44
print(dicc4)

# Para recuperar la clave
for elemento in dicc1:
    print(elemento)

print("\n")

# Para recuperar los valores
for elemento in dicc1:
    print(dicc1[elemento])

print("\n")

# Para recuperar la clave y el valor
for elemento in dicc1:
    print(elemento, ":", dicc1[elemento])

print("\n")

# Para recuperar la clave y el valor
for clave, valor in dicc1.items():
    print(clave, ":", valor)

print("\n")

# Para recuperar valores unicos
print(dicc1["Edad"])
print(dicc1.get("Edad"))
print(dicc1.get("Edad2")) # Te dara none al no existir

# El segundo parametro es opcional, sirve para que nos devuelva lo que queramos, hasta parametros booleanos
print(dicc1.get("Titulo", "No encontrado"))


# Modifica el valor de Edad, siempre que exista, si no existe lo añade, como en el ejemplo de abajo
dicc1["Edad"] = 44
print(dicc1["Edad"])


# Si no existe el valor, lo añade
dicc1["Asignatura"] = "Bases de Datos"
print(dicc1)


# Devuelve las claves
print(dicc3.keys())

# Devuelve los valores
print(dicc3.values())

# Actualizacion masiva, si hay un elemento duplicado lo sustituye, y si no, metes a todos en el diccionario
dicc1.update(dicc3)
print(dicc1)

# Sirve para eliminar el elementos -> .pop
print(dicc1.pop("Edad"))
print(dicc1)

# Sirve para eliminar el ultimo elemento insertado -> .popitem, en este caso es el de segundo: dos
print(dicc1.popitem())
print(dicc1)


# Elimina completamerte el diccionario = .clear()
dicc1.clear()
print(dicc1)