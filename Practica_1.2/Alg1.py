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
    if arreglo[n-2] == -1:
        arreglo[n-2] = fibo3(n-2, arreglo)
    
    arreglo[n] = arreglo[n-1] + arreglo[n-2]
    return arreglo[n]




if __name__ == '__main__':

    f = open("Runtimes_table_2-3.txt", "a")

    f.write("N      Algoritmo 2     Algoritmo 3\n")
    
    for n in range(100):
        
        # inicio = time()
        # fibo1(n)
        # final = time()
        # tiempo1 = (final-inicio)*1000

        inicio = time()
        arreglo1 = [0 for i in range(n+1)]
        fibo2(n, arreglo1)
        final = time()
        tiempo1 = (final-inicio)*1000

        inicio = time()
        arreglo = [-1 for i in range(n+1)]
        fibo3(n, arreglo)
        final = time()
        tiempo2 = (final-inicio)*1000

        f.write('{}     {}      {}\n'.format(n,tiempo1,tiempo2))

    f.close()