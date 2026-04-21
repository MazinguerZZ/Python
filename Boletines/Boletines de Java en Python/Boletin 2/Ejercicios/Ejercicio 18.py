# Escribe un programa que le pida al usuario su sueldo anual (lógicamente puede ser
# un número con decimales) y le informe que porcentaje de retención le corresponde, el
# importe de la misma y el importe neto restante que cobrará.

sueldo = float(input("Ingrese el sueldo: "))
if 0 <= sueldo <= 12450:
    print("La retención que le corresponde es de un 19%")
    importe_retenido = sueldo * 0.19
    print("Importe que se retendrá: ", round(importe_retenido, 2))
    print("Importe neto que cobraras: ", round(sueldo - importe_retenido, 2))
elif 12450 <= sueldo <= 20200:
    print("La retención que le corresponde es de un 24%")
    importe_retenido = sueldo * 0.24
    print("Importe que se retendrá: ", round(importe_retenido, 2))
    print("Importe neto que cobraras: ", round(sueldo - importe_retenido, 2))
elif 20200 <= sueldo <= 35200:
    print("La retención que le corresponde es de un 30%")
    importe_retenido = sueldo * 0.3
    print("Importe que se retendrá: ", round(importe_retenido, 2))
    print("Importe neto que cobraras: ", round(sueldo - importe_retenido, 2))
elif 35200 <= sueldo <= 60000:
    print("La retención que le corresponde es de un 37%")
    importe_retenido = sueldo * 0.37
    print("Importe que se retendrá: ", round(importe_retenido, 2))
    print("Importe neto que cobraras: ", round(sueldo - importe_retenido, 2))
elif 60000 <= sueldo <= 300000:
    print("La retención que le corresponde es de un 45%")
    importe_retenido = sueldo * 0.45
    print("Importe que se retendrá: ", round(importe_retenido, 2))
    print("Importe neto que cobraras: ", round(sueldo - importe_retenido, 2))
elif sueldo >= 300000:
    print("La retención que le corresponde es de un 47%")
    importe_retenido = sueldo * 0.47
    print("Importe que se retendrá: ", round(importe_retenido, 2))
    print("Importe neto que cobraras: ", round(sueldo - importe_retenido, 2))

