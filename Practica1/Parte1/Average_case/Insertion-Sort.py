from time import time

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
    
    print('Insertion Sort Algorithm')

    dato1 = open('datos1.txt', 'w')

    for i in range(1000, 10000+1, 1000):

        A = []
        file_name = 'scripts/random_'+str(i)+'.txt'

        f = open(file_name, 'r')
        for x in f:
            A.append(int(x))

        tiempo_ejecucion = InsertionSort(A)
        dato1.write(str(i)+' '+str(tiempo_ejecucion)+'\n')
    
    print('Archivo Creado')
