# Crea una clase que almacene una lista con los días de la semana y un índice que indique el día actual.
# La clase debe poder mostrarse por pantalla y también debe ser iterable: cada llamada a next() devolverá el día actual y
# avanzará al siguiente, volviendo al inicio cuando llegue al final.

class DiasDeLaSemana:
    # Constructor
    def __init__(self, dia):
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.diaDeHoy = dia

    def mostrar(self):
        print(self.dias[self.diaDeHoy])

    # Crea un iterador de esta clase
    def __iter__(self):
        return self

    def __next__(self):
        # if self.diaDeHoy >= len(self.dias):
        #     raise StopIteration
        dia_actual = self.dias[self.diaDeHoy]
        if self.diaDeHoy == len(self.dias)-1:
            self.diaDeHoy = 0
        else:
            self.diaDeHoy += 1
        return dia_actual

dia = DiasDeLaSemana(2)
# dia.mostrar()

iterador = iter(dia)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

