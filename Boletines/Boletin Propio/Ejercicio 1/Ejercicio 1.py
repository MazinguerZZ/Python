# 13. Conversión de números romanos a enteros
# Los números romanos se representan mediante siete símbolos diferentes:  I, V, X, L, C, Dy M.
#
#           Valor del símbolo
#           Yo 1
#           V 5
#           X 10
#           L 50
#           C 100
#           D 500
#           M 1000

# Por ejemplo,  2se escribe como II en números romanos, simplemente dos unos sumados. 12se escribe como  XII, que es simplemente X + II. El número 27se escribe como XXVII, que es XX + V + II.
#
# Los números romanos se suelen escribir de mayor a menor, de izquierda a derecha. Sin embargo, el número cuatro no es IIII. En cambio, el número cuatro se escribe como IV. Como el uno está antes del cinco, lo restamos, obteniendo cuatro. El mismo principio se aplica al número nueve, que se escribe como IX. Hay seis casos en los que se utiliza la resta:
#
# I se puede colocar antes de V(5) y X(10) para formar 4 y 9.
# X se puede colocar antes de L(50) y C(100) para formar 40 y 90.
# C se puede colocar antes de D(500) y M(1000) para hacer 400 y 900.
# Dado un número romano, conviértalo a un número entero.
#

def conversorRomano(letra):
    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    prev = 0

    for i in reversed(letra):
        valor = valores[i]
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor

    return total

print(conversorRomano("IV"))
print(conversorRomano("IX"))
print(conversorRomano("XIII"))