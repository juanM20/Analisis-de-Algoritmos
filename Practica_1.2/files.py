from time import time


def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n-1) + fibo1(n-2)


if __name__ == '__main__':
    
    f = open("Algoritmo1.txt", "w")

    f.write("N  Algoritmo 1\n")
    
    for n in range(45):

        inicio = time()
        fibo1(n)
        final = time()
        tiempo = (final-inicio)*1000

        f.write("{} {}\n".format(n, tiempo))
        
    