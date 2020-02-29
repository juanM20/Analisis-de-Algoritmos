from time import time
import random

def Random_arrays(n):
    arr = []
    for i in range(n):
        i=i
        arr.append(random.randint(1,100))
    return arr 



def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]    # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

def QuickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        QuickSort(arr, low, pi-1) 
        QuickSort(arr, pi+1, high) 


if __name__ == '__main__':
    
    file = open('QuickSort.txt', 'w')
    file.write('\tQuickSort\n\n')
    file.write('Number of elements   Execution time\n')
    
    for n in range(1000,11000,1000):
        array = []
        array = Random_arrays(n)
        init_time = time()
        QuickSort(array,0,len(array)-1)
        final_time = time()
        execution_time = (final_time-init_time) * 1000
        file.write('{}  {}\n'.format(n,execution_time))