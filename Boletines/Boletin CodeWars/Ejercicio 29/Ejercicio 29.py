def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)

print(area_or_perimeter(4,4))
print(area_or_perimeter(6,10))