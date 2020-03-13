


def Mochila(tabla, Peso_Mochila, objetos):

    maximo = 0
    cant_objeto = len(objetos)
    a,b = 0,0

    tabla = [[0 for j in range(Peso_Mochila + 1)] for i in range(cant_objeto)]

    for i in range(0,cant_objeto,1):
        for j in range(1,Peso_Mochila+1,1):
            
            if i-1 < 0:
                tabla[i][j] += objetos[i][1]

            elif j-objetos[i][0] < 0:
                tabla[i][j] = tabla[i-1][j]
            
            else:

                a = tabla[i-1][j]
                b = tabla[i-1][j - objetos[i][0]] + objetos[i][1]

                if a > b:
                    tabla[i][j] = a
                else:
                    tabla[i][j] = b

    for i in range(0,cant_objeto,1):
        print("\n")
        for j in range(0,Peso_Mochila+1,1):
            print(tabla[i][j], end=" ")
    
    maximo = tabla[cant_objeto-1][Peso_Mochila]

    return maximo


if __name__ == "__main__":
    
    tabla = []
    objetos = [
        [1,1],
        [2,6],
        [5,18],
        [6,22],
        [7,28]
    ]

    Peso_Mochila = int(input("Peso que soporta la mochila: "))

    resultado = Mochila(tabla, Peso_Mochila, objetos)
    print("\nValor maximo: "+str(resultado))