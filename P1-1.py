
def BubbleSort(A):
    n = len(A)
    swapped = False
    while not swapped:
        for i in range(n):
            if A[i-1] > A[i]:
                aux = A[i-1]
                A[i-1] = A[i]
                A[i] = aux
                swapped = True
        n = n-1
    
    return A




if __name__ == "__main__":
    A = [2,5,3,7,2312,6,73,6343,732,83,1]
    
    BubbleSort(A)
    
    print(A)