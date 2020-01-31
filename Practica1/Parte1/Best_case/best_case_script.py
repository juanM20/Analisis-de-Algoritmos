import random
import sys

def creaValor(n):
    lista  = []
    for i in range(0, n):
        lista.append(i)
    return lista

def escribeArchivo(file, lista):
    f = open (file, "w")
    for e in lista:
        f.write("%d\n" % e)

    f.close()


if len(sys.argv) != 2:
    print("Execute python bes_case_script.py [numero de elementos]")
else:
    elementos = (int)(sys.argv[1])
    lista = creaValor(elementos)
    nameFile = "best_" + str(elementos) + ".txt"
    escribeArchivo(nameFile, lista)


