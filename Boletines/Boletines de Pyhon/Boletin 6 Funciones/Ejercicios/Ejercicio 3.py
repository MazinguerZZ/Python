# 3. Escribir una función en python que reciba una cadena de texto y un carácter y la escriba al
# revés y suprimiendo las apariciones de ese caracter.
# EJEMPLO DE EJECUCIÓN:
#           INVOCACIÓN DE LA FUNCIÓN                    RESULTADO EN LA CONSOLA
#           volteayelmimina(“Hola mundo cruel”, “o”)    La cadena al revés y sin el
#                                                       carácter ‘o’ es: leurc
#                                                       dnum alH
#                                                       He eliminado 2 caracteres
from idlelib import replace


def volteayelimina(texto, caracter):
    cadena = texto[::-1]
    contador = 0

    for i in cadena:
        if i == caracter:
            cadena = str(cadena).replace(f"{caracter}", "")
            contador += 1
    print(f"La cadena al revés y sin el carácter ‘{caracter}’ es: {cadena}")
    print(f"He eliminado {contador} caracteres")

volteayelimina("Hola mundo cruel", "o")



