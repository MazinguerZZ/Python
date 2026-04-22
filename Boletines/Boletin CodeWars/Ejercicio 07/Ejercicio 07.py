def disemvowel(string_):
    reemplazo = (string_.replace("a", "").replace("A", "").
                        replace("e", "").replace("E", "").
                        replace("i", "").replace("I", "").
                        replace("o", "").replace("O", "").
                        replace("u", "").replace("U", ""))
    return reemplazo

print(disemvowel("This website is for losers LOL!"))