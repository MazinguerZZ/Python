# Dada una cadena s, devuelve la cadena después de reemplazar cada letra mayúscula
# con la misma letra minúscula.

def cadenaInvertida(s):
    texto = str(s)
    return texto.lower()

print(cadenaInvertida("Hello"))
print(cadenaInvertida("ESPAÑA"))