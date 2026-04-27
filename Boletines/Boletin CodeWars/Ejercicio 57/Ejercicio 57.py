def name_shuffler(str_):
    partes = str_.split(" ")
    return f"{partes[1]} {partes[0]}"

print(name_shuffler("Alvarez Adrian"))
