# Idem al anterior pero ordenando ahora en orden descendente

texto = input("Primera palabra: ")
texto2 = input("Segunda palabra: ")
texto3 = input("Tercera palabra: ")
orden_min = min(texto, texto2, texto3)
orden_mid = texto+texto2+texto3
orden_mid = orden_mid.replace(min(texto, texto2, texto3), "",1)
orden_mid = orden_mid.replace(max(texto, texto2, texto3), "",1)
orden_max = max(texto, texto2, texto3)
print(orden_max, orden_mid, orden_min)