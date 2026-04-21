#  Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
# vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”

texto = (input("Ingrese un texto: ").
         replace("a", "").replace("A", "").
         replace("e", "").replace("E", "").
         replace("i", "").replace("I", "").
         replace("o", "").replace("O", "").
         replace("u", "").replace("U", ""))
print(texto)