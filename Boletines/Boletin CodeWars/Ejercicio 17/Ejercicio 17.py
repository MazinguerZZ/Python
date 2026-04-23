import re

def valid_phone_number(phone_number):
    regex = r"\((\d{3})\) \d{3}-\d{4}$"
    if re.match(regex, phone_number):
        return True
    else:
        return False

print(valid_phone_number("(123) 456-7890"))
print(valid_phone_number("(1111)555 2345"))
print(valid_phone_number("abc(123) 456-7890abc"))