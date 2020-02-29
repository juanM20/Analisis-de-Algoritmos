from Coordenada import Coordenada

class Reina:
    n=8
    def __init__(self, coord, tamTablero): #Coordenada coord
        if isinstance(coord, Coordenada) and isinstance(tamTablero, int):
            self.coord= coord
            #self.n= tamTablero
        else:
            self.coord= Coordenada(1, 1)
            #self.n= 4

    def obtCoordenada(self):
        return self.coord
    
    def defCoordenada(self, newCoord):
        if isinstance(newCoord, Coordenada):
            self.coord= newCoord

    def ataqueRecto(self, reinaAtak):
        if isinstance(reinaAtak, Reina):
            if self.obtCoordenada().obtX() == reinaAtak.obtCoordenada().obtX() or self.obtCoordenada().obtY() == reinaAtak.obtCoordenada().obtY():
                return True
            
    def ataqueDiagonalSD(self, reinaAtak): #Ataque diag. superior derecho
        auxCoord= Coordenada(0, 0)
        auxCoord.definir(self.obtCoordenada()) #Guardamos la coordenada original para restaurarlo después de su modificación para pruebas
        ret= True

        #DIAGONAL SUPERIOR DERECHA
        if not (self.obtCoordenada().obtX()==self.n or self.obtCoordenada().obtY()==self.n):
            while not (self.obtCoordenada().obtX()>self.n-1 or self.obtCoordenada().obtY()>self.n-1): #menor que el tablero
                if not self.obtCoordenada().equals(reinaAtak.obtCoordenada()): #si las coordenadas son diferentes
                    self.obtCoordenada().desplazarDiagSupDer(1)
                    #print("ABCD")
                    ret= False
                    #self.verCoord()
                else: 
                    #print("CDEF")
                    ret= True
                    break #Si las coordenadas son iguales, entocnes se rompe el ciclo y se devuelve ret inicial
        
            self.defCoordenada(auxCoord) #Regresamos el valor original
            if ret:
                #print("Ataque: DSD") #DSD, DSI, DID, DII
                auxRet=ret
        else:
            ret=False

        return ret
        
    def ataqueDiagonalID(self, reinaAtak): #Ataque diag. inferior derecho
        auxCoord= Coordenada(0, 0)
        auxCoord.definir(self.obtCoordenada()) #Guardamos la coordenada original para restaurarlo después de su modificación para pruebas
        ret= True

        #DIAGONAL INFERIOR DERECHA
        if not (self.obtCoordenada().obtX()==self.n or self.obtCoordenada().obtY()==1):
            while not (self.obtCoordenada().obtX()>self.n-1 or self.obtCoordenada().obtY()<2): #menor que el tablero
                if not self.obtCoordenada().equals(reinaAtak.obtCoordenada()): #si las coordenadas son diferentes
                    self.obtCoordenada().desplazarDiagInfDer(1)
                    ret= False
                    #self.verCoord()
                else: 
                    ret= True
                    break #Si las coordenadas son iguales, entocnes se rompe el ciclo y se devuelve ret inicial

            self.defCoordenada(auxCoord) #Regresamos el valor original
            if ret:
                #print("Ataque: DID") #DSD, DSI, DID, DII
                auxRet=ret
        else:
            ret=False
        
        return ret

    def ataqueDiagonalSI(self, reinaAtak): #Ataque diag. superior izquierdo
        auxCoord= Coordenada(0, 0)
        auxCoord.definir(self.obtCoordenada()) #Guardamos la coordenada original para restaurarlo después de su modificación para pruebas
        ret= True

        #DIAGONAL SUPERIOR IZQUIERDA
        if not (self.obtCoordenada().obtX()==1 or self.obtCoordenada().obtY()==self.n):
            while not (self.obtCoordenada().obtX()<2 or self.obtCoordenada().obtY()>self.n-1): #menor que el tablero
                if not self.obtCoordenada().equals(reinaAtak.obtCoordenada()): #si las coordenadas son diferentes
                    self.obtCoordenada().desplazarDiagSupIzq(1)
                    ret= False
                    #self.verCoord()
                else: 
                    ret= True
                    break #Si las coordenadas son iguales, entocnes se rompe el ciclo y se devuelve ret inicial

            self.defCoordenada(auxCoord) #Regresamos el valor original
            if ret:
                #print("Ataque: DSI") #DSD, DSI, DID, DII
                auxRet=ret
        else:
            ret=False

        return ret

    def ataqueDiagonalII(self, reinaAtak): #Ataque diag. inferior izquiera
        auxCoord= Coordenada(0, 0)
        auxCoord.definir(self.obtCoordenada()) #Guardamos la coordenada original para restaurarlo después de su modificación para pruebas
        ret= True

        #DIAGONAL INFERIOR IZQUIERDA
        if not (self.obtCoordenada().obtX()==1 or self.obtCoordenada().obtY()==1):
            while not (self.obtCoordenada().obtX()<2 or self.obtCoordenada().obtY()<2): #menor que el tablero
                if not self.obtCoordenada().equals(reinaAtak.obtCoordenada()): #si las coordenadas son diferentes
                    self.obtCoordenada().desplazarDiagInfIzq(1)
                    ret= False
                    #self.verCoord()
                else: 
                    ret= True
                    break #Si las coordenadas son iguales, entocnes se rompe el ciclo y se devuelve ret inicial

            self.defCoordenada(auxCoord) #Regresamos el valor original
            if ret:
                #print("Ataque: DII") #DSD, DSI, DID, DII
                auxRet=ret
        else:
            ret=False
        
        return ret

    def verCoord(self):
        print(self.coord.toString())

    def equals(self, r):
        if isinstance(r, Reina):
            if self.obtCoordenada().equals(r.obtCoordenada()):
                return True



    

