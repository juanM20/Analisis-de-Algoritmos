from time import time

def InsertionSort(A):
    for i in range(1, len(A)):
        j = i-1
        while j >= 0 and A[j] > A[j+1]:
            aux = A[j]
            A[j] = A[j+1]
            A[j+1] = aux
            j = j-1

    return A






if __name__ == "__main__":
    A = [2,5,3,7,2312,6,73,6343,732,83,1]
    
    t1 = time()
    InsertionSort(A)
    t = time() - t1

    print('\nTiempo de ejecucion %0.5f' %t )

    print(A)
