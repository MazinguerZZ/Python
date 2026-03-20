# Escribir un programa que reciba por teclado un número y muestre sucesivamente el
# resultado de ir dividiéndolo por dos sucesivamente hasta llegar a un número igual o menor a
# 1. Caso de ser necesario los resultados se mostrarán con dos decimales. Un ejemplo de una
# ejecución correcta después de introducir el número 34 ser´ía esta:

num= float(input("Indica el numero: "))
while num>=1:
    num=num/2
    print(round(num, 2))