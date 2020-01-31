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

    print(A)
       
    return tiempo_ejecucion



if __name__ == '__main__':
        
    A = [6,2,9,4,7,1,33,91,3]
        
    t = BubbleSort(A)
    print(t)
        