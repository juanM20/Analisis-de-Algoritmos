from Mochila import Mochila
from Objeto import Objeto

def Mayor_Elemento(lista, peso, W):
    mayor = 0
    bueno=0
    aux = 0
    auxPos=0
    for i in range(len(lista)):
        if  lista[i].getPeso()+peso <= W:
            aux = lista[i].getVpup()
        else:
            if lista[i].getValor()>lista[i-1].getValor():
                bueno = lista[i].getVpup()
                auxPos=i

        if aux > mayor:
            mayor = aux
            bueno = mayor
            auxPos=i
            
    return (bueno, lista[auxPos].getPeso(), auxPos)

def mochila(lista, W):
    xSel= [0 for i in range(0,len(lista))] #lista de Vpup finales
    auxLista= lista
    suma=0 #suma de pesos
    while suma<W:
        
        x = Mayor_Elemento(auxLista,suma, W)

        if suma+x[1]<=W:
            xSel[x[2]]=1
            suma+=x[1]
            auxLista[x[2]]=Objeto(1,0) #sustituir por uno de valor=0 para que Vpup=0
        else:
            xSel[x[2]]=(W-suma)/x[1] #Tomar una fracción del objeto
            suma=W
            auxLista[(x[2])]=Objeto(1,0)        
        
    return xSel

m= Mochila(100, 5) #Capacidad W=100, n=5 objetos
o= [Objeto(10, 20), Objeto(20, 30), Objeto(30, 66), Objeto(40, 40), Objeto(50, 60)] #Objeto(peso, valor)
o2= [Objeto(10, 20), Objeto(20, 30), Objeto(30, 66), Objeto(40, 40), Objeto(50, 60)]

oAux=[]
for i in range(0, len(o)):
    oAux.append(o[i].getValor())

res= mochila(o, m.getCapacidad())
valorTotal=0
for i in range(0, len(o)):
    valorTotal+= oAux[i]*res[i]

print("Objetos disponibles: ")
for i in range(0, len(o)):
    print(o2[i].toString())
print("\nValor en la mochila: "+str(valorTotal)+"u")





