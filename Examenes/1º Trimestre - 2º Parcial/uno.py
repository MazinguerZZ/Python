def devuelveLinea(n):
    n = n - 1
    if n==-1:
        n=9
    linea=""
    for posicion in range(10):
        if posicion == n:
            linea += "0"
        else:
            linea += "x"
    return linea

def cifradoPin(pin):
    pinTxT = str(pin)
    for _ in range(len(pinTxT),4):
        pinTxT = "0" + pinTxT
    lista = []
    for c in pinTxT:
        lista.append(devuelveLinea(int(c)))
    return tuple(lista)

pin = 5678
resultado = cifradoPin(pin)
print(f"PIN: {pin}")
print("Representación:")
for linea in resultado:
    print(linea)