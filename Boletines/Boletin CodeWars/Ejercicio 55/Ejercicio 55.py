def are_you_playing_banjo(name):
    primer_caracter = name[0]
    if primer_caracter == "R" or primer_caracter == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("Ramon"))
print(are_you_playing_banjo("raul"))
print(are_you_playing_banjo("Adrian"))