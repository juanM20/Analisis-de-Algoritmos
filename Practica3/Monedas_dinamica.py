
def Cambio(tabla, N, denominaciones):
    
    minimo = 0
    cant_denominaciones = len(denominaciones)

    tabla = [ [0 for j in range(N+1)] for i in range(cant_denominaciones) ]

    for i in range(0,cant_denominaciones,1):
        for j in range(1,N+1,1):

            if i-1 < 0:
                tabla[i][j] = tabla[i][j-denominaciones[i]] + 1
            elif j-denominaciones[i] < 0:
                tabla[i][j] = tabla[i-1][j]
            elif i-1 >= 0 and j-denominaciones[i] >= 0:
        
                if tabla[i-1][j] < tabla[i][j-denominaciones[i]] + 1:
                    tabla[i][j] = tabla[i-1][j]
                else:
                    tabla[i][j] = tabla[i][j-denominaciones[i]] + 1
    
    minimo = tabla[cant_denominaciones-1][N]

    for i in range(0,cant_denominaciones,1):
        print("\n")
        for j in range(0,N+1,1):
            print(str(tabla[i][j]), end=" ")

    return minimo



if __name__ == "__main__":

    tabla = []
    denominaciones = [1,2,5,10]
    N = int(input('Numero a cambiar: '))
    
    resultado = Cambio(tabla, N, denominaciones)
    print("\n\nLa menor cantidad de monedas es: "+str(resultado))
