import random
import sys

def creaValor(n):
    lista  = []
    for i in range(n-1, -1, -1):
        lista.append(i)
    return lista

def escribeArchivo(file, lista):
    f = open (file, "w")
    for e in lista:
        f.write("%d\n" % e)

    f.close()


if len(sys.argv) != 2:
    print("Execute python aleatorios.py [numero de elementos]")
else:
    elementos = (int)(sys.argv[1])
    lista = creaValor(elementos)
    nameFile = "worst_" + str(elementos) + ".txt"
    escribeArchivo(nameFile, lista)

