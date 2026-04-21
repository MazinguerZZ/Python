# Escribir un programa que reciba por teclado una temperatura en cualquiera de las
# tres unidades básicas (Celcius, Farenheit o Kelvin) y la devuelva en las otras dos.
# Tu programa reconocerá la unidad que has usado al introducir la entrada por teclado
# porque irá acompañado de una letra que lo indique. Por ejemplo, 12C, 280.57K o
# 98.6F
# Se admitirán decimales en la entrada, (como se ve en los ejemplos anteriores) y se
# devolverá el resultado con dos decimales
# Las formulas de conversión entre unidades son las siguientes:
# Para convertir de ºC a ºF use la fórmula: ºF = ºC x 1.8 + 32.
# Para convertir de ºF a ºC use la fórmula: ºC = (ºF-32) ÷ 1.8.
# Para convertir de ºK a ºC use la fórmula: ºC = ºK – 273.15
# Para convertir de ºC a ºK use la fórmula: ºK = ºC + 273.15.
# Para convertir de ºF a ºK use la fórmula: ºK = 5/9 * (ºF – 32) + 273.15.
# Para convertir de ºK a ºF use la fórmula: ºF = 1.8(ºK – 273.15) + 32.

temperatura = input("Ingrese la temperatura (Celcius, Farenheit o Kelvin): ")

valor = temperatura[:-1]
unidad = temperatura[-1]

temperatura = float(valor)

celcius = "C"
farenheit = "F"
kelvin = "K"

if unidad.upper() in "C":
    print("La temperatura en Farenheit es: ", round(temperatura * 1.8 + 32, 2))
    print("La temperatura en Kelvin es: ", round(temperatura + 273.15, 2))

if unidad.upper() in "F":
    print("La temperatura en Celcius es: ", round((temperatura-32) / 1.8, 2))
    print("La temperatura en Kelvin es: ", round(5/9 * (temperatura - 32) + 273.15, 2))

if unidad.upper() in "K":
    print("La temperatura en Celcius es: ", round(temperatura - 273.15, 2))
    print("La temperatura en Farenheit es: ", round(1.8 * (temperatura - 273.15) + 32, 2))