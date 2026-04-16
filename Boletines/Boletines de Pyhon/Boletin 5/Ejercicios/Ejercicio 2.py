# 2. Escribir un programa que nos pida el nombre, el nombre de la asignatura y las notas de
# un alumno de cada uno de los tres trimestres y lo almacene todo en una lista. Luego lo
# debería de mostrar todo en pantalla junto con la media que correspondería a la nota
# final. Un ejemplo de la salida por pantalla sería así:
# Nombre: José María Morales
# Asignatura: Python
# Nota del primer trimestre: 8.5
# Nota del segundo trimestre: 9.5
# Nota del tercer trimestre: 10.0
# Nota media final: 9.0

nombre = input("Introduce tu nombre: ")
asignatura = input("Introduce tu asignatura: ")
nota_trimestre1 = int(input("Introduce tu nota del primer trimestre: "))
nota_trimestre2 = int(input("Introduce tu nota del segundo trimestre: "))
nota_trimestre3 = int(input("Introduce tu nota del tercer trimestre: "))

lista = [nombre, asignatura, nota_trimestre1, nota_trimestre2, nota_trimestre3]

print("Nombre:", lista[0])
print("Asignatura:", lista[1])
print("Nota del primer trimestre:", lista[2])
print("Nota del segundo trimestre:", lista[3])
print("Nota del tercer trimestre:", lista[4])
nota = round(((lista[2] + lista[3] + lista[4]) / 3), 2)
print("Nota media final:", nota)


