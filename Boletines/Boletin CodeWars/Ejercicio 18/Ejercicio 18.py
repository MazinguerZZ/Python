def multi_table(number):
    result = ""
    for i in range(1,11):
        resultado = i * number
        result += f"{i} * {number} = {resultado}\n"
    return result.rstrip()

print(multi_table(5))