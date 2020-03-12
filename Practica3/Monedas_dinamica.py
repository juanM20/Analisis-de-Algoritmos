class Moneda:

    def __init__(self, cantidad, diccionario):
        self.cantidad = cantidad
        self.diccionario = diccionario




def Cambio(tabla, N, denominaciones):
    
    minimo = 0
    conjunto_monedas = {}
    cant_denominaciones = len(denominaciones)

    cantidad_aux = 0
    diccionario_aux = {}

    tabla = [ [0 for j in range(N+1)] for i in range(cant_denominaciones) ]

    for i in range(0,cant_denominaciones,1):
        for j in range(0,N+1,1):

            dic = {
            }

            tabla[i][j] = Moneda(0,dic)

    for i in range(0,cant_denominaciones,1):
        for j in range(1,N+1,1):

            cantidad_aux = 0
            diccionario_aux.clear()

            if i-1 < 0:
                cantidad_aux = tabla[i][j-denominaciones[i]].cantidad + 1
                diccionario_aux = tabla[i][j-denominaciones[i]].diccionario.copy()
                
                if str(denominaciones[i]) in diccionario_aux:
                    diccionario_aux[str(denominaciones[i])] += 1
                else:
                    diccionario_aux[str(denominaciones[i])] = 1

                tabla[i][j] = Moneda(cantidad_aux, diccionario_aux.copy())


            elif j-denominaciones[i] < 0:
                cantidad_aux = tabla[i-1][j].cantidad
                diccionario_aux = tabla[i-1][j].diccionario.copy()

                tabla[i][j] = Moneda(cantidad_aux, diccionario_aux.copy())


            elif i-1 >= 0 and j-denominaciones[i] >= 0:
        
                if tabla[i-1][j].cantidad < tabla[i][j-denominaciones[i]].cantidad + 1:
                    cantidad_aux = tabla[i-1][j].cantidad
                    diccionario_aux = tabla[i-1][j].diccionario.copy()

                    tabla[i][j] = Moneda(cantidad_aux, diccionario_aux.copy())


                else:
                    cantidad_aux = tabla[i][j-denominaciones[i]].cantidad + 1
                    diccionario_aux = tabla[i][j-denominaciones[i]].diccionario.copy()
                    
                    if str(denominaciones[i]) in diccionario_aux:
                        diccionario_aux[str(denominaciones[i])] += 1
                    else:
                        diccionario_aux[str(denominaciones[i])] = 1

                    tabla[i][j] = Moneda(cantidad_aux, diccionario_aux.copy())

    
    minimo = tabla[cant_denominaciones-1][N].cantidad
    conjunto_monedas = tabla[cant_denominaciones-1][N].diccionario.copy()

    for i in range(0,cant_denominaciones,1):
        print("\n")
        for j in range(0,N+1,1):
            print(str(tabla[i][j].cantidad)+" "+str(tabla[i][j].diccionario), end=" ")

    return [minimo,conjunto_monedas]



if __name__ == "__main__":

    tabla = []
    denominaciones = [1,2,5,10]
    N = int(input('Numero a cambiar: '))
    
    resultado = Cambio(tabla, N, denominaciones)
    print("\nLa menor cantidad de monedas es: "+str(resultado[0]))
    print("\nConjunto de monedas: " +str(resultado[1]))
