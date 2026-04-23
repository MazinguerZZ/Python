def is_uppercase(inp):
    for char in inp:
        if char.isalpha() and char.islower():
            return False
    return True

print(is_uppercase("c"))
print(is_uppercase("C"))
print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("HELLO I AM DONALD"))
print(is_uppercase("$%&"))