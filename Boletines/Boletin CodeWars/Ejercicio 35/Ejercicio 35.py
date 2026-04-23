def calculator(x, y, op):
    x = str(x)
    y = str(y)
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"

print(calculator(6, "$", "+"))
print(calculator(4, 3, '-'))
print(calculator(5, 5, '*'))
print(calculator(5, 4, '/'))
print(calculator(6, 2, '&'))