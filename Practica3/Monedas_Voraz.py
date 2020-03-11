
def Mayor_Elemento(D, suma, n):

    mayor = 0
    aux = 0
    for i in range(len(D)):
        if  D[i]+suma <= n:
            aux = D[i]
        if aux > mayor:
            mayor = aux
    return mayor

def Devolver(D, n):
    M = []
    suma=0
    while not suma==n:
        
        x = Mayor_Elemento(D,suma, n)

        if x not in D:
            print("No encuentro la solución")
            break
        else:
            M.append(x)
            suma+=x

    return M

    
if __name__ == "__main__":
    
    D1= [100, 25, 2, 5]
    D2= [6, 4, 1]

    print("Para D1:")
    print("Cambio de 8: "+str(Devolver(D1,8)))
    print("Cambio de 25: "+str(Devolver(D1,25)))
    print("Cambio de 47: "+str(Devolver(D1,47)))
    print("Cambio de 642: "+str(Devolver(D1,642)))
    print("Cambio de 1025: "+str(Devolver(D1,1025)))
    print("Cambio de 356: "+str(Devolver(D1,356)))
    print("\n\n")
    print("Para D2:")
    print("Cambio de 8: "+str(Devolver(D2,8)))
    print("Cambio de 25: "+str(Devolver(D2,25)))
    print("Cambio de 47: "+str(Devolver(D2,47)))
    print("Cambio de 642: "+str(Devolver(D2,642)))
    print("Cambio de 1025: "+str(Devolver(D2,1025)))
    print("Cambio de 356: "+str(Devolver(D2,356)))