# FORMA 1

# def toDecimal(cadena_binario):
#     try:
#         decimal = int(cadena_binario, 2)
#         valor = decimal
#     except ValueError:
#         valor = -1
#     return valor
#
# print(toDecimal("10110"))
# print(toDecimal("345"))
# print(toDecimal("hola"))



# FORMA 2

def toDecimal(binario):
    es_binario = True
    for i in range(len(binario)):
        if binario[i] != '0' and binario[i] != '1':
            es_binario = False
    if es_binario == True:
        binario = list(binario)
        binario.reverse()
        decimal = 0
        for i in range(len(binario)):
            decimal = decimal + int(binario[i]) * (2 ** i)
        return decimal
    else:
        return -1

print(toDecimal("10110"))
print(toDecimal("345"))
print(toDecimal("hola"))