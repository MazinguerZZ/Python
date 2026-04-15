# 4. Escribir un programa en python que nos pida las notas obtenidas en un trimestre y nos
# muestre la media ponderada sabiendo que;
# ◦ La primera nota corresponde al trabajo en clase y cuenta como un 10% del total
# ◦ La segunda corresponde a los ejercicios prácticos: 20%
# ◦ La tercera la nota del examen: 70%

nota_trabajo = int(input("Dime la nota del trabajo en clase: "))
nota_practicas = int(input("Dime la nota de las practicas: "))
nota_examen = int(input("Dime la nota del examen: "))

nota_final_trabajo = nota_trabajo * 0.1
nota_final_practicas = nota_practicas * 0.2
nota_final_examen = nota_examen * 0.7

media_aritmetica = nota_final_trabajo + nota_final_practicas + nota_final_examen
print("La nota media es: ", media_aritmetica)