nombre = "Jose Maria"
edad = 57
sueldo = 1200.567
ficha = f"""
Ficha del profesor
==========================
Nombre: {nombre}
Edad: {edad}
Sueldo: {sueldo:.2f} euros
==========================
"""
print(ficha)
# f""" (contenido) """ = Tambien sirve como f-String

print("Mi nombre es", nombre, "tengo", edad, "años y cobro", sueldo, "euros")
print("Mi nombre es %s tengo %d años y cobro %.2f euros" %(nombre, edad, sueldo))
# %s = Tipo String
# %d = Tipo entero
# %f = Tipo float
# %.2f = Para redondear a 2 decimales

print(f"Mi nombre es {nombre} tengo {edad} años y cobro {sueldo:.2f} euros")
# {sueldo:.2f} = Para redondear a 2 decimales

promedio = 0.86754
print(f"El porcentaje de aprovados es de {promedio:.2%}")
poblacion = 1234567890
print(f"La poblacion del pais es de {poblacion:,} habitantes")

n1 = 23
n2 = 456
n3 = 1
lista = [1,2,3]
print(f"Numeros: \n{n1:04d}\n{n2:04d}\n{n3:04d}")
# {n1:04d} = añade 0
print(f"Justificando a la izquierda: ***{n1:<20}***")
# ***{n1:<20}*** =  mueve 20 espacios a la izquierda los 3 ultimos asterixcos
print(f"Justificando a la derecha: ***{n1:>20}***")
# ***{n1:>20}*** =  mueve 20 espacios a la derecha los 3 ultimos asterixcos
print(f"Justificando a la derecha: ***{n1:^20}***")
# ***{n1:^20}*** =  estara centrado, 10 a la izquierda y 10 a la derecha

print(f"Inspeccionando variables {n1=} y {n2=}")
# {n1=} = Para que devuelva el valor de la variable
print(f"Inspeccionando variables {lista=}")

def devuelveMiNombre():
    return "Jose Maria"

print(f"Mi nombre es: {devuelveMiNombre()}")
# Con funciones tambien sirve

print(f"¿n1 es par? {True if n1%2==0 else False}")
print(f"¿n2 es par? {'Si' if n2%2==0 else 'No'}")
# Se pueden hacer condiciones
nota = 4
print(f"Nota: {'Excelente' if nota > 8 else 'Suficiente' if nota > 5 else 'Suspenso'}")