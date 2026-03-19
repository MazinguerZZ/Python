from abc import abstractmethod, ABC


class ClaseAbstracta(metaclass=ABC):
    def metodoChorra(self):
        print("Hola", "Hola")


    @abstractmethod
    def metodoAbstracto(self):
        pass
nuevo = ClaseAbstracta()
nuevo.metodoChorra()
