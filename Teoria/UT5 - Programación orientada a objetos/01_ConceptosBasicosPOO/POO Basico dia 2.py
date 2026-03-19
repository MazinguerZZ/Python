# Esto sirve para guardar datos, la clase la iniciamos vacia y despues de van añadiendo datos
class Empleado:
    pass

empleado1 = Empleado()
empleado1.nombre = "Jose Maria"
empleado1.apellidos = "Morales Vazquez"
empleado1.edad = 57
empleado1.activo = True

print(empleado1.apellidos, ",", empleado1.nombre)