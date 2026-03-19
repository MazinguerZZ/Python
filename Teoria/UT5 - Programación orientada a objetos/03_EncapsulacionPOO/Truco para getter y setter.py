# Si ponemos "prop", se genera solo el getter

class prueba:

    @property
    def indice(self):
        return

# Si ponemos "props", se genera el getter y el setter

    @property
    def indice(self):
        return

    @indice.setter
    def indice(self, value):
        pass