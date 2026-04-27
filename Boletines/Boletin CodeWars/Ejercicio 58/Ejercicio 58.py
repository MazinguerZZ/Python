def find_unique(numbers):
    unicos = 0
    for i in numbers:
        unicos ^= i
    return unicos

print(find_unique([1, 8, 4, 4, 6, 1, 8]))
print(find_unique(list(range(1, 1_000_000))*2 + [1234567]))