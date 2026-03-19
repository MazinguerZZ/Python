profesores = ["Agustin", "Natalia", "Javier"]
iterador = iter(profesores)
# Nos da el siguiente elemento de la lista
print(next(iterador))
print(next(iterador))
print(next(iterador))
# Si no hay, da una excepcion, pero si ponemos un texto informativo no da excepcion ni error, solo el mensaje
print(next(iterador, "No hay mas profes"))
