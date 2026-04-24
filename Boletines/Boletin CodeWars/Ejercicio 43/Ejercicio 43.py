def find_needle(haystack):
    stack = haystack.index("needle")
    return f"found the needle at position {stack}"

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))