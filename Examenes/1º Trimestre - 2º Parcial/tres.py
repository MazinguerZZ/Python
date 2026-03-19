import re

def validar(matricula):
    patron = r"[0-9]{4}[\s|-]?[B-DF-HJ-NP-TV-Z]{3}"
    matricula = matricula.upper()
    if re.fullmatch(patron,matricula):
        correcto = True
    else:
        correcto = False
    return correcto

def matriculasValidas(*matriculas):
    total = 0
    validas = 0
    for m in matriculas:
        total += 1
        correcto = validar(m)
        if correcto == True:
            print(m, "- Válida")
            validas += 1
        else:
            print(m, "- Inválida")

    print("Resumen:", validas, "válidas de", total, "matriculas")
    return validas


resultado = matriculasValidas("1234ABC", "5678-BCD", "9999XYZ", "0000 AAA", "1111LMN")
print("Valor retornado:", resultado)