def odd_or_even(arr):
    if not arr:
        return "even"
    elif sum(arr) % 2 != 0:
        return "odd"
    else:
        return "even"

print(odd_or_even([0, 1, 2]))
print(odd_or_even([0, 1, 3]))
print(odd_or_even([1023, 1, 2]))