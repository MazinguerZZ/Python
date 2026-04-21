# Dado un entero no negativo x, devuelve la raíz cuadrada de x redondeada hacia abajo al entero más cercano . El entero devuelto también debe ser no negativo .
#
# No debe utilizar ninguna función u operador de exponente incorporado.
import math
from math import trunc


def mySqrt(x):
    raiz = math.sqrt(x)
    return trunc(raiz)

print(mySqrt(8))
