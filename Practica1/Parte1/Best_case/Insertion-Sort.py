from time import time
import os

def InsertionSort(A):

    inicio = time()

    for i in range(1, len(A)):
        j = i-1
        while j >= 0 and A[j] > A[j+1]:
            aux = A[j]
            A[j] = A[j+1]
            A[j+1] = aux
            j = j-1

    final = time()
    tiempo_ejecucion = (final-inicio)*1000

    return tiempo_ejecucion



if __name__ == "__main__":

    cont = 0

    print('Insertion Sort Algorithm')

    for i in range(1000, 10000+1, 1000):
        cmd = "python best_case_script.py " +str(i) 
        os.system(cmd)
        cont += 1
        print('Archivo {} creado'.format(cont))


    dato1 = open('dato1_best_case.txt', 'w')

    for i in range(1000, 10000+1, 1000):

        A = []
        file_name = 'best_'+str(i)+'.txt'

        f = open(file_name, 'r')
        for x in f:
            A.append(int(x))

        tiempo_ejecucion = InsertionSort(A)
        dato1.write(str(i)+' '+str(tiempo_ejecucion)+'\n')
    
    print('Archivo Creado')
