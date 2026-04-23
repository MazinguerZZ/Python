def correct(s):
    texto = (str(s).replace("5", "S").
                    replace("0", "O").
                    replace("1", "I"))
    return texto

print(correct("L0ND0N"))
