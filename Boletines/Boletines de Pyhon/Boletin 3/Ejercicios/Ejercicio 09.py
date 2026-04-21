# 19. Escribe un programa en Python que le pida al usuario su sueldo anual (puede ser un
# número con decimales) y le informe que porcentaje de retención le corresponde, el
# importe de la misma y el importe neto restante que cobrará.

sueldo = float(input("Introduce tu sueldo actual: "))

if sueldo < 12450:
    print("Se le aplicará un porcenatje del 19%.")
    print("El importe que se le retiene es de:", round(sueldo * 0.19, 2), "€")
    print("El importe neto que cobrara sera de:", round(sueldo - sueldo * 0.19, 2), "€")
elif 12450 < sueldo < 20200:
    print("Se le aplicará un porcenatje del 24%.")
    print("El importe que se le retiene es de:", round(sueldo * 0.24, 2), "€")
    print("El importe neto que cobrara sera de:", round(sueldo - sueldo * 0.24, 2), "€")
elif 20200 < sueldo < 35200:
    print("Se le aplicará un porcenatje del 30%.")
    print("El importe que se le retiene es de:", round(sueldo * 0.30, 2), "€")
    print("El importe neto que cobrara sera de:", round(sueldo - sueldo * 0.30, 2), "€")
elif 35200 < sueldo < 60000:
    print("Se le aplicará un porcenatje del 37%.")
    print("El importe que se le retiene es de:", round(sueldo * 0.37, 2), "€")
    print("El importe neto que cobrara sera de:", round(sueldo - sueldo * 0.37, 2), "€")
elif 60000 < sueldo < 300000:
    print("Se le aplicará un porcenatje del 45%.")
    print("El importe que se le retiene es de:", round(sueldo * 0.45, 2), "€")
    print("El importe neto que cobrara sera de:", round(sueldo - sueldo * 0.45, 2), "€")
elif sueldo > 300000:
    print("Se le aplicará un porcenatje del 47%.")
    print("El importe que se le retiene es de:", round(sueldo * 0.47, 2), "€")
    print("El importe neto que cobrara sera de:", round(sueldo - sueldo * 0.47, 2), "€")
