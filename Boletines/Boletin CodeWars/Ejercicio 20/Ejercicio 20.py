def correct_polish_letters(st):
    linea_española = (st.replace("ą", "a").replace("ć", "c").replace("ę", "e").
                      replace("ł", "l").replace("ń", "n").replace("ó", "o").
                      replace("ś", "s").replace("ź", "z").replace("ż", "z"))
    return linea_española


print(correct_polish_letters("Jędrzej Błądziński"))