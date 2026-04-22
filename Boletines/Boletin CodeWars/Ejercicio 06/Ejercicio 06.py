def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        milisegundos = h * 3600000 + m * 60000 + s * 1000
        return milisegundos
    return None

print(past(0, 1 , 1))
