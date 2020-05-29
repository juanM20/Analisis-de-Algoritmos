import numpy as np


def LCS_Length(X,Y):

    m , n = len(X), len(Y)
    c , b = np.zeros((m+1,n+1)), np.zeros((m+1,n+1))

    for i in range(m):
        for j in range(n):
            
            if X[i] == Y[j]:
                c[i+1,j+1] = c[i,j] + 1 
                b[i+1,j+1] = 1
            
            elif c[i,j+1] >= c[i+1,j]:
                c[i+1,j+1] = c[i,j+1]
                b[i+1,j+1] = 2
            
            else:
                c[i+1,j+1] = c[i+1,j]
                b[i+1,j+1] = 3 
    
    print(c)
    print('\n')
    print(b)

    return c,b

def Print_LCS(b,X,i,j):

    if i==0 or j==0 :
        return 
    
    if b[i,j] == 1 :
        Print_LCS(b,X,i-1,j-1)
        print(X[i-1])
    
    elif b[i,j] == 2 :
        Print_LCS(b,X,i-1,j)

    else:
        Print_LCS(b,X,i,j-1) 



X = ['A','B','C','B','D','A','B']
Y = ['B','D','C','A','B','A']

c,b = LCS_Length(X,Y)

print('\n')
Print_LCS(b,X,len(X),len(Y))






