def plural(n):
    if n == 0 or n >= 2:
        return True
    else:
        return False

print(plural(0))
print(plural(1))
print(plural(100))