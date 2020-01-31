from time import time

def BubbleSort(A):

    inicio = time()

    n = len(A)
    while True:
        swapped = False
        for i in range(1, n):
            if A[i-1] > A[i]:
                aux = A[i]
                A[i] = A[i-1]
                A[i-1] = aux
                swapped = True
        n = n-1
        if not swapped:
            break

    final = time()
    tiempo_ejecucion = (final-inicio)*1000
       
    return tiempo_ejecucion




if __name__ == "__main__":
    print('Bubble Sort Algorithm')

    dato2 = open('datos2.txt', 'w')

    for i in range(1000,10000+1, 1000):

        A = []
        file_name = 'scripts/random_'+str(i)+'.txt'

        f = open(file_name, 'r')
        for x in f:
            A.append(int(x))

        tiempo_ejecucion =  BubbleSort(A)
        dato2.write(str(i)+' '+str(tiempo_ejecucion)+'\n')

    print('Archivo creado')
