class Objeto:
    def __init__(self, peso, valor):
        self.w=peso
        self.v=valor
        self.vpup= valor/peso

    def getVpup(self): #Valor por unidad de peso
        return self.vpup

    def setVpup(self, vpup): #Valor por unidad de peso
        self.vpup= vpup

    def getPeso(self):
        return self.w
    
    def getValor(self):
        return self.v

    def toString(self):
        return "O[w:"+str(self.getPeso())+", v:"+str(self.getValor())+"]"
#obj= Objeto(30, 66)
#print(obj.getVpup())
    