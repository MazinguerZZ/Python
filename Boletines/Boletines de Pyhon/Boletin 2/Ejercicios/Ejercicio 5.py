# 5. Modifica el ejercicio anterior para que cuando la media salga como aprobado pero el
# alumno tenga menos de un 4,5 en cualquiera de los apartados la nota resultante será
# un 4

nota_trabajo = float(input("Dime la nota del trabajo en clase: "))
nota_practicas = float(input("Dime la nota de las practicas: "))
nota_examen = float(input("Dime la nota del examen: "))

nota_final_trabajo = nota_trabajo * 0.1
nota_final_practicas = nota_practicas * 0.2
nota_final_examen = nota_examen * 0.7

media_aritmetica = nota_final_trabajo + nota_final_practicas + nota_final_examen

if nota_trabajo < 4.5:
    print("La nota media es un 4")
elif nota_practicas < 4.5:
    print("La nota media es un 4")
elif nota_examen < 4.5:
    print("La nota final es un 4")
else:
    print("La nota media es: ", media_aritmetica)

