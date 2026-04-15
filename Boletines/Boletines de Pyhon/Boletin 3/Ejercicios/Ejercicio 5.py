# 5. Escribir un programa python que reciba una cadena de texto y la muestre sin vocales.
# Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”.

texto = input("Introduce una frase: ")

texto_sin_vocales = (texto.replace("a", "").replace("A", "").
                    replace("e", "").replace("E", "").
                    replace("i", "").replace("I", "").
                    replace("o", "").replace("O", "").
                    replace("u", "").replace("U", ""))

print(texto_sin_vocales)