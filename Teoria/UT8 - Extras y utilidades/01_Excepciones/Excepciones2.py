from cgi import print_form

n = int(input("Introduceme un numero entero positivo: "))
# if n<0:
#     raise Exception("No es un entero positivo") # Forzamos la excepcion y sale el texto en la excepcion
# print(n)

# raise ZeroDivisionError("No has dividido por cero pero lo digo yo") # RAISE para forzar la excepcion

# assert n==1, "El numero no me gusta" # Si es verdad, pa alante, sino, excepcion que te da, tambien funciona con parentesis
assert n>0, "El numero no es positivo"