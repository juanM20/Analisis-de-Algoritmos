class Mochila:
    def __init__(self, capacidad, nObjetos):
        self.W= capacidad
        self.n= nObjetos

    def getCapacidad(self):
        return self.W

    def getNObjetos(self):
        return self.n