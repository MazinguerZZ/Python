def esPalindromo(x):
    if x < 0:
        return False

    s = str(x)
    return s == s[::-1]

print(esPalindromo(121))
print(esPalindromo(-121))
print(esPalindromo(10))
