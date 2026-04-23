def hello(name=""):
    if not name:
        return f"Hello, World!"
    else:
        nombre = str(name).capitalize()
        return f"Hello, {nombre}!"

print(hello())