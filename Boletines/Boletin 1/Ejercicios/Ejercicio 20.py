# Escribir un programa que nos pida tres números por teclado en cualquier orden y nos los
# muestre en pantalla ordenados de menor a mayor

numero = int(input("Dame el primer numero: "))
numero2 = int(input("Dame el segundo numero: "))
numero3 = int(input("Dame el tercer numero: "))

val_max = max(numero, numero2, numero3)
val_min = min(numero, numero2, numero3)
val_mid = (numero + numero2 + numero3) - val_min - val_max

print("El ordes es: " , val_min, "," , val_mid, "," ,val_max)