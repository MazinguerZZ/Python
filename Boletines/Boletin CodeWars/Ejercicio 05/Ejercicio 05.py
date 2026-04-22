def remove_exclamation_marks(s):
    return s.replace("!", "").replace("¡", "")

print(remove_exclamation_marks("¡Hello World!"))