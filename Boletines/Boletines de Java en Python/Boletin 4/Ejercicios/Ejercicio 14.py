# 14. Escribe un programa que lea una hora por teclado en formato 24 horas (HH:MM). Tu
# programa debería de decir si corresponde a la mañana (entre las 6 y las 11, ambas
# inclusive), si es una hora de la tarde (entre las 12 y las 19, ambas inclusive), si es de la
# noche (entre las 20 y las 23, ambas inclusive), si es de la madrugada (entre las 0 y las
# 5, ambas inclusive) o bien, si el formato no es correcto o no se corresponde con una
# hora real (minutos de mas de 60, horas negativas o por encima de 23, etc.

try:
    tiempo = input("Ingrese la hora para saber que momento del dia es: ")

    partes = tiempo.split(":")
    hora = partes[0]
    minutos = partes[1]

    if 0 <= int(minutos) < 60 and 0 <= int(hora) <= 23:
        if 6 <= int(hora) <= 11:
            print("Es por la mañana.")
        elif 12 <= int(hora) <= 19:
            print("Es por la tarde.")
        elif 20 <= int(hora) <= 23:
            print("Es por la noche.")
        elif 0 <= int(hora) <= 5:
            print("Es por la madrugada.")
    else:
        print("La hora no es valida.")
except Exception as e:
    print("Error: ", e)