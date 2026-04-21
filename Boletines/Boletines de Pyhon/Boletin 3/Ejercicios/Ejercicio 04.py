# 4. Escribir un programa que pida al usuario una cadena de texto y la escriba con el
# alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
# el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
# las vocales pueden estar escritas en mayúsculas o minúsculas y tiene que funcionar con
# ambas, pero no hace falta que tengas en cuenta que además podrían ir acentuadas

texto = input("Introduce una frase: ")

texto_codificado = (texto.replace("a", "4").replace("A", "4").
                    replace("e", "3").replace("E", "3").
                    replace("i", "1").replace("I", "1").
                    replace("o", "0").replace("O", "0"))

print(texto_codificado)