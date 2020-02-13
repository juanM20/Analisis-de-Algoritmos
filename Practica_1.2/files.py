from time import time


def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n-1) + fibo1(n-2)


if __name__ == '__main__':
    
    inicio = time()
    fibo1(40)
    final = time()
    print((final-inicio)*1000)
    