# Ejercicio 1 – RA1 y RA2 (1,5 puntos)
# Después de perder varias partidas al Fortnite estás convencido de cuál ha sido
# el problema: no conoces las matemáticas detrás del cierre del círculo seguro
# en la tormenta.
# Dispuesto a mejorar para las próximas, te has propuesto escribir un programa
# en Python que pida al usuario el radio de la zona segura por teclado, calcule
# su área y muestre el resultado por pantalla. (1 punto)
# Pero el programa podría estar aún más completo. Para el circulo final el radio
# ha disminuido en un 60% respecto a su tamaño inicial, teniendo que recalcular
# el área antes de mostrar su nuevo tamaño por pantalla. (0,5 puntos)

radio = float(input("Introduce el radio de la zona: "))
area = 3.1416 * (radio**2)
print(f"El area del circulo es de {round(area, 2)}")

area2 = 3.1416 * ((radio - (radio * 0.6)) ** 2)
print(f"El area circulo final es de {round(area2, 2)}")