from time import time

def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n-1) + fibo1(n-2)


def fibo2(n,arreglo):
    
    if n < 2:
        return n
    else: 
        
        arreglo[0] = 0
        arreglo[1] = 1
        for i in range(2,n+1):
            arreglo[i] = arreglo[i-1] + arreglo[i-2]

        return arreglo[n]

def fibo3(n, arreglo):

    if n < 2:
        return n
    
    if arreglo[n-1] == -1:
        arreglo[n-1] = fibo3(n-1, arreglo)
        arreglo[1] = 1
        i=1
        for i in range(n):
            arreglo[i] = arreglo[i-1] + arreglo[i-2]
        return arreglo[n-1]




if __name__ == '__main__':

    f = open("Runtimes_table.txt", "a")

    f.write("N      Algoritmo 1     Algoritmo 2\n")
    
    for n in range(5,100,5):
        
        inicio = time()
        fibo1(n)
        final = time()
        tiempo1 = (final-inicio)*1000

        inicio = time()
        arreglo1 = [0 for i in range(n+1)]
        fibo2(n, arreglo1)
        final = time()
        tiempo2 = (final-inicio)*1000

        f.write('{}     {}      {}'.format(n,tiempo1,tiempo2))

        # arreglo = [-1 for i in range(n)]
        # print(fibo3(n, arreglo))

    f.close()