from time import time
import os

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

    cont = 0

    print('Bubble Sort Algorithm')

    for i in range(1000, 10000+1, 1000):
        cmd = "python best_case_script.py " +str(i) 
        os.system(cmd)
        cont += 1
        print('Archivo {} creado'.format(cont))

    dato2 = open('datos2_best_case.txt', 'w')

    for i in range(1000,10000+1, 1000):

        A = []
        file_name = 'best_'+str(i)+'.txt'

        f = open(file_name, 'r')
        for x in f:
            A.append(int(x))

        tiempo_ejecucion =  BubbleSort(A)
        dato2.write(str(i)+' '+str(tiempo_ejecucion)+'\n')

    print('Archivo creado')
