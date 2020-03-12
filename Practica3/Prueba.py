class Moneda:
    
    def __init__(self, cantidad, diccionario):
        self.cantidad = cantidad
        self.diccionario = diccionario

    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def setDiccionario(self, diccionario):
        self.diccionario = diccionario
    




if __name__ == '__main__':
    
    tabla = [ [0 for j in range(9)] for i in range(3) ]


    for i in range(0,3,1):
        for j in range(0,9,1):

            dic = {
            }

            tabla[i][j] = Moneda(0,dic)

    
    for i in range(0,3,1):
        print("\n")
        for j in range(0,9,1):
            print(str(tabla[i][j].cantidad)+" "+str(tabla[i][j].diccionario), end=" ")