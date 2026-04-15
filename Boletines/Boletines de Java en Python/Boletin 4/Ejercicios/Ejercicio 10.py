# 10. Escribir un programa que nos pida una cadena por teclado y luego nos imprima sólo
# las cifras que aparecen en ella.
# Por ejemplo, si introducimos la cadena “Beverly Hills, 5. CP: 28934” Debería
# devolvernos: 528934

texto = input("Ingrese una frase: ")
numero = texto.isdigit()

for i in texto:
    if i.isdigit():
        print(i, end="")