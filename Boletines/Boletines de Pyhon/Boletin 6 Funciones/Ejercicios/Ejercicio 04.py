# 4. Escribir una función en python que reciba una cadena de texto que representa una fracción y
# nos devuelva su valor en decimal. La fracción tiene que ser introducida con el formato:
# numerador/denominador, siendo numerador y denominador dos números enteros. Si
# introducimos algo que no corresponda con esto debería de devolver un cero

# EJEMPLOS DE EJECUCIÓN:
#           INVOCACIÓN DE LA FUNCIÓN            RESULTADO EN LA CONSOLA
#           print(fraccion(“25/10”))            2.5
#           print(fracción(“a/10”))             0
#           print(fracción(“//10”))             0
#           print(fracción(“10”))               0

def fraccion(texto):
    try:
        partes = texto.split("/")

        if len(partes) != 2:
            return 0

        numerador = int(partes[0])
        denominador = int(partes[1])

        return numerador / denominador
    except ValueError:
        return 0


print(fraccion("25/10"))
print(fraccion("a/10"))
print(fraccion("//10"))
print(fraccion("10"))
