class Coordenada:
    #x= {A, B, ..., Z}
    #y= {1, 2, ..., n}, índices: 0 a n-1

    def __init__(self, x, y): #Formato: [<Letra>, <Número>]
        if isinstance(x, int) and isinstance(y, int) and x>0 and y>0:
            self.x= x
            self.y= y
        else:
            self.x= 1
            self.y= 1
            #print("Coordenada no válida, creado default (A1)")

    def definir(self, nValor):
        if isinstance(nValor, Coordenada):
            self.x= nValor.obtX()
            self.y= nValor.obtY()

    def obtX(self):
        return self.x
    def obtY(self):
        return self.y

    def desplazarDer(self, n):
        self.x+=n

    def desplazarIzq(self, n):
        self.x-=n

    def desplazarArr(self, n):
        self.y+=n

    def desplazarAba(self, n):
        self.y-=n
    
    def desplazarDiagSupDer(self, n): #desplazar en el primer cuadrante
        self.desplazarDer(n)
        self.desplazarArr(n)
    
    def desplazarDiagSupIzq(self, n): #desplazar en el segundo cuadrante
        self.desplazarIzq(n)
        self.desplazarArr(n)

    def desplazarDiagInfIzq(self, n): #desplazar en el tercer cuadrante
        self.desplazarIzq(n)
        self.desplazarAba(n)

    def desplazarDiagInfDer(self, n): #desplazar en el cuarto cuadrante
        self.desplazarDer(n)
        self.desplazarAba(n)

    def toString(self):
        return "["+str(self.x)+", "+str(self.y)+"]"

    def equals(self, c):
        if isinstance(c, Coordenada):
            if self.obtX()==c.obtX() and self.obtY()==c.obtY():
                return True


    def pruebas(self): #Esto va a en el tablero
        letraX=[]
        n=7
        if n>26: n= 91+(n-26)
        else: n= 65+n
        
        for i in range(65,n):
            letraX.append(str(chr(i)))
        

        print(letraX)
    
    

