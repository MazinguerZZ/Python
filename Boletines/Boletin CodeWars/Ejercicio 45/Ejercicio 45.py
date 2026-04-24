def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)

print(find_average([1, 2, 3]))
print(find_average([]))