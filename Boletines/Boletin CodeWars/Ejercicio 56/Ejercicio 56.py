import string

def is_pangram(st):
    es_pangrama = set(string.ascii_lowercase) <= set(st.lower())
    if es_pangrama == True:
        return True
    else:
        return False