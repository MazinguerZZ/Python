# Escribe un programa que pida por teclado el radio de una circunferencia, admitiendo
# valores con decimales y calcule la longitud y el área de la circunferencia (redondeando
# a cinco decimales). Si no las recuerdas, las fórmulas son las siguientes:
# area = 3.14159 * radio2
# longitud = 2 * 3.14159 * radio

radio = float(input("Ingrese el radio de la circunferencia: "))

print("Area: ", round(radio * 3.14159, 5))
print("Longitud: ", round(2 * 3.14159 * radio, 5))