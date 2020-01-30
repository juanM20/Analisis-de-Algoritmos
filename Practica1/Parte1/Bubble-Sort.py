from time import time

def BubbleSort(A):

    inicio = time()

    n = len(A)
    for k in range(0, n-1):
        for i in range(0, n-1-k):
            if A[i] > A[i+1]:
                aux = A[i]
                A[i] = A[i+1]
                A[i+1] = aux

    final = time()
    tiempo_ejecucion = (final-inicio)*1000
       
    return tiempo_ejecucion




if __name__ == "__main__":
    print('Bubble Sort Algorithm')

    dato2 = open('datos2.txt', 'w')

    for i in range(1000,10000+1, 100):

        A = []
        file_name = 'scripts/random_'+str(i)+'.txt'

        f = open(file_name, 'r')
        for x in f:
            A.append(int(x))

        tiempo_ejecucion =  BubbleSort(A)
        dato2.write(str(i)+' '+str(tiempo_ejecucion)+'\n')

    print('Archivo creado')
