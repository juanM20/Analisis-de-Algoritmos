import numpy as np
import sys
from time import time


def writeFile(ruta, content):
    f = open (ruta+".txt", "a")
    f.flush()
    f.write(str(content)+"\n")
    f.close()

def readFile(ruta):
    lista= []
    file = open (ruta, "r")
    
    while True:
        linea= file.readline()

        if linea!='':
            if(linea!='\n'):
                lista.append(linea)
        else:
            break

    file.close()

    return lista[0], lista[1]

def LCS_Length(X,Y):

    m , n = len(X), len(Y)
    c , b = np.zeros((m+1,n+1)), np.zeros((m+1,n+1))

    for i in range(m):
        for j in range(n):
            
            if X[i] == Y[j]:
                c[i+1,j+1] = c[i,j] + 1 
                b[i+1,j+1] = 1
            
            elif c[i,j+1] >= c[i+1,j]:
                c[i+1,j+1] = c[i,j+1]
                b[i+1,j+1] = 2
            
            else:
                c[i+1,j+1] = c[i+1,j]
                b[i+1,j+1] = 3 
    
    # print(c)
    # print('\n')
    # print(b)

    return c,b

def Print_LCS(b,X,i,j,lcs):

    if i==0 or j==0 :
        return 
    
    if b[i,j] == 1 :
        Print_LCS(b,X,i-1,j-1,lcs)
        lcs.append(X[i-1])
    
    elif b[i,j] == 2 :
        Print_LCS(b,X,i-1,j,lcs)

    else:
        Print_LCS(b,X,i,j-1,lcs) 




if __name__ == '__main__':
    
    ######PRUEBA##################
    """X = 'ABCBDAB'
    Y = 'BDCABA'
    lcs = []

    c,b = LCS_Length(X,Y)

    print('\n')
    Print_LCS(b,X,len(X),len(Y),lcs)
    print(lcs)
    print('Porcentaje de coincidencia: {}%'.format(round((len(lcs)/len(X))*100,2)))"""
    ##############################

    if len(sys.argv) != 3:
        print("Faltan o sobran argumentos: [nombre_archivo_fuente nombre_archivo_salida(sin_extension)]")
    else:
        X, Y= readFile(sys.argv[1])
        lcs = []

        initTime= time()
        c,b = LCS_Length(X,Y)
        endTime= time()

        Print_LCS(b,X,len(X),len(Y),lcs)

        runTime= (endTime-initTime)*1000



        writeFile(sys.argv[2], "Matriz:")
        writeFile(sys.argv[2], str(c))
        writeFile(sys.argv[2], "\nCoincidencia:")
        writeFile(sys.argv[2], "".join(lcs))
        writeFile(sys.argv[2], "\nPorcentaje de coincidencia: {}%".format(round((len(lcs)/len(X))*100,2)))
        writeFile(sys.argv[2], "\nTiempo de ejecución del algoritmo: %0.15f ms" % runTime)  



