def mouth_size(animal):
    resultado = animal.lower()
    if resultado == "alligator":
        return "small"
    else:
        return "wide"

print(mouth_size("toucan"))
print(mouth_size("ant bear"))
print(mouth_size("alligator"))