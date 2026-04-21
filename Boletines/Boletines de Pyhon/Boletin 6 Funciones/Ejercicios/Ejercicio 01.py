# 1. Escribir una función en python que reciba dos argumentos: el precio y el iva y nos calcule y
# devuelva el pvp una vez aplicado el iva con dos decimales
# EJEMPLOS DE EJECUCIÓN:
#       INVOCACIÓN DE LA FUNCIÓN              RESULTADO EN LA CONSOLA
#       print(pvp(14, 0))                     14
#       print(pvp(34.4 ,21))                  41.62

def pvp(precio, iva):
    return round(precio * (iva / 100) + precio, 2)

print(pvp(34.4, 21))
