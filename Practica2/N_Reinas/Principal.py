from Coordenada import Coordenada
from Reina import Reina
from random import randint
import sys


def escribirArchivo(ruta, info):
    f = open (ruta, "a")
    f.flush()
    f.write(str(info)+"\n")
    f.close()


def generarTotalReinas(tTablero, arrayReinas):
    for i in range(0, tTablero): #recorre la lista y
        while True: 
           generada= Reina(Coordenada(randint(1, tTablero), randint(1, tTablero)), tTablero) #quédate generando reinas,
           if generada not in arrayReinas: #si esa reina no está en la lista,
                arrayReinas.append(generada) #entonces agrégala
                break


def generarReinasConPrevias(reinasPrev, tTablero, arrayReinas):
    for i in range(reinasPrev, tTablero): #recorre la lista y
        while True: 
           generada= Reina(Coordenada(randint(1, tTablero), randint(1, tTablero)), tTablero) #quédate generando reinas,
           if generada not in arrayReinas: #si esa reina no está en la lista,
                arrayReinas.append(generada) #entonces agrégala
                break

def exitos(contador, chequeos):
    return str((contador*100)/chequeos)


misReinas= []
misSoluciones= []

if len(sys.argv) != 4:
    print("Faltan argumentos: [tamaño_tablero] [num_reinas_previas] [num_revisiones]")
else:

    #tamTab= int(input("Tamaño del tablero: "))
    #tamTab=8
    tamTab= (int)(sys.argv[1])

    #numReinasPrevias= int(input("Número de reinas previas en el tablero: "))
    numReinasPrevias= (int)(sys.argv[2])

    #nCheck= int(input("Número de revisiones: "))
    nCheck= (int)(sys.argv[3])
    
    if numReinasPrevias==0:
        generarTotalReinas(tamTab, misReinas)
    else:
        for i in range(0, numReinasPrevias):
            x= int(input("\nCoordenada X reina "+str(i+1)+": "))
            y= int(input("Coordenada Y reina "+str(i+1)+": "))
            misReinas.append(Reina(Coordenada(x, y), tamTab))

        generarReinasConPrevias(numReinasPrevias, tamTab, misReinas)
    


    #Una solución:
    """
    reina1= Reina(Coordenada(1, 2), tamTab)
    reina2= Reina(Coordenada(4, 8), tamTab)
    reina3= Reina(Coordenada(6, 1), tamTab)
    reina4= Reina(Coordenada(2, 4), tamTab)
    reina5= Reina(Coordenada(8, 5), tamTab)
    reina6= Reina(Coordenada(7, 7), tamTab)
    reina7= Reina(Coordenada(5, 3), tamTab)
    reina8= Reina(Coordenada(3, 6), tamTab)

    misReinas.append(reina1)
    misReinas.append(reina2)
    misReinas.append(reina3)
    misReinas.append(reina4)
    misReinas.append(reina5)
    misReinas.append(reina6)
    misReinas.append(reina7)
    misReinas.append(reina8)
    """

    o=0 #indicador de la posición de misReinas para las comapraciones
    j=1 #indicador para el número de chequeo de soluciones
    bndValid= True #Bandera de validación para escribir solución en el archivo
    contaExitos=0

    for i in range(0, len(misReinas)):
        print("Reina "+str(i+1)+": "+misReinas[i].obtCoordenada().toString())

    while True:
        print("-----------------CHEQUEO NÚMERO "+str(j)+"-----------------")
        while o<len(misReinas):
            compara= misReinas[o]

            #print("\nREINA "+str(o+1))
            for i in range(0, len(misReinas)):
                if not compara.equals(misReinas[i]): #Para que no se compare a sí misma
                    if compara.ataqueRecto(misReinas[i]):
                        bndValid=False
                        #print("Hay ataque recto")
                    else:
                        if compara.ataqueDiagonalSI(misReinas[i]) or compara.ataqueDiagonalSD(misReinas[i]) or compara.ataqueDiagonalII(misReinas[i]) or compara.ataqueDiagonalID(misReinas[i]):
                            bndValid=False
                            #print("Hay ataque diagonal")
            o+=1
        if bndValid:
            # Formato de soluciones en archivod e texto: [X, Y], las X deberían ser caracteres, pero por cuestiones de practicidad, se manejaron enteros
            for i in range(0, len(misReinas)):
                misSoluciones.append(misReinas[i].obtCoordenada().toString())
            escribirArchivo("Soluciones"+str(nCheck)+".txt", misSoluciones)
            contaExitos+=1
            misSoluciones.clear()
        for i in range(numReinasPrevias, len(misReinas)): #Eliminar las reinas aleatorias para generar nuevas conservando las predefinidas
            misReinas.pop()

        if not numReinasPrevias==tamTab: #Si las reinas previas son el total de reinas, no va a generar más piezas
            generarReinasConPrevias(numReinasPrevias, tamTab, misReinas)

        o=0 #Reiniciar contador de reinas

        j+=1 #Siguiente revisión

        if j>nCheck:
            break


    print("\n\nExito de "+exitos(contaExitos, nCheck)+"%")

