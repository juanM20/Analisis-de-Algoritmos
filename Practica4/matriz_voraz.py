from time import time

class Matrix:
    def __init__(self, label, rows, columns):
        self.label = label
        self.rows = rows
        self.columns = columns
    
    def Show_matrix(self):
        return '{}: {}x{}'.format(self.label,self.rows,self.columns)

def get_lists(matrix_array):
    
    list1 = matrix_array
    list2 = matrix_array

    list1 = sorted(list1,key=lambda x: x.columns, reverse=True)
    list2 = sorted(list2,key=lambda x: x.rows, reverse=True)

    return list1,list2

def Search_Ak(Aj, list2):

    Ak_index = -1

    for matrix in list2:
        if matrix.columns == Aj.rows:
            return list2.index(matrix)
    
    return Ak_index

def buscar_indices(list1):

    list1.reverse()

    Aj=-1
    Ak=-1

    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i].rows == list1[j].columns:
                Aj=i
                Ak=j
                return Aj,Ak
    return Aj,Ak 

def Voraz(matrix_array):

    list1,list2 = get_lists(matrix_array)

    Suma = 0
    i = len(list1)-1
    cont = 0

    while(len(list1) > 1):

        Aj = list1[i]
        Ak_index = Search_Ak(Aj, list2)
        
        if Ak_index != -1:
            
            # Si se encuentra una matriz Ak en la lista 2
            # Se realiza el producto de Ak*Aj
            Ak = list2[Ak_index]
            cont += 1
            label = 'B'+str(cont)
            rows = Ak.rows
            columns = Aj.columns
            new_matrix = Matrix(label,rows,columns)

            # Calculamos la cantidad de operacioens que se realizan
            Suma += Ak.rows*Ak.columns*Aj.columns

            # Guardar los labels de la multplicación
            # PENDIENTE

            # Borrar Ak y Aj de las listas
            list1.remove(Ak)
            list1.remove(Aj)
            if Ak in list2:
                list2.remove(Ak)
            if Aj in list2:
                list2.remove(Aj)

            # Insertar la matriz resultante de la multiplicación de Ak * Aj
            list1.append(new_matrix)
            list1 = sorted(list1, key=lambda x: x.columns, reverse=True)

            i = len(list1)-1

        else:

            if i >= 0:
                i -= 1
            else:

                Aj_indice,Ak_indice = buscar_indices(list1)
               
                if Aj_indice!=-1 and Ak_indice!=-1:

                    Aj = list1[Aj_indice]
                    Ak = list1[Ak_indice]

                    cont += 1
                    label = 'B'+str(cont)
                    rows = Ak.rows
                    columns = Aj.columns
                    new_matrix = Matrix(label,rows,columns)
  
                    Suma += Ak.rows*Ak.columns*Aj.columns
                        
                    list1.remove(Ak)
                    list1.remove(Aj)
                    if Ak in list2:
                        list2.remove(Ak)
                    if Aj in list2:
                        list2.remove(Aj)
                    
                    list1.append(new_matrix)
                    list1 = sorted(list1, key=lambda x: x.columns, reverse=True)

                    i=len(list1)-1
                
                else:
                    print("No existe asociación")
                    exit()

    print("\nSuma: {}".format(Suma))
    
    return Suma


if __name__ == '__main__':

    # m1 = Matrix('A1',30,35)
    # m2 = Matrix('A2',35,15)
    # m3 = Matrix('A3',15,5)
    # m4 = Matrix('A4',5,10)
    # m5 = Matrix('A5',10,20)
    # m6 = Matrix('A6',20,25)

    n1 = Matrix('A1',50,30)
    n2 = Matrix('A2',30,20)
    n3 = Matrix('A3',20,100)

    m1 = Matrix('A1',10,200)
    m2 = Matrix('A2',200,300)
    m3 = Matrix('A3',300,50)
    m4 = Matrix('A4',50,90)
    m5 = Matrix('A5',90,10)

    b1 = Matrix('A1',1,2)
    b2 = Matrix('A2',2,3)
    b3 = Matrix('A3',3,4)
    b4 = Matrix('A4',4,5)
    b5 = Matrix('A5',5,6)
    b6 = Matrix('A6',6,7)

    matrix_array1 = [n1,n2,n3]
    matrix_array2 = [m1,m2,m3,m4,m5]
    matrix_array3 = [b1,b2,b3,b4,b5,b6]

    cant_operation_list = []
    time_execution_list = []

    t1 = time()
    cant = Voraz(matrix_array1)
    t2 = time()

    cant_operation_list.append(cant)
    time_execution_list.append((t2-t1)*1000)

    t1 = time()
    cant = Voraz(matrix_array2)
    t2 = time()

    cant_operation_list.append(cant)
    time_execution_list.append((t2-t1)*1000)
    
    t1 = time()
    cant = Voraz(matrix_array3)
    t2 = time()

    cant_operation_list.append(cant)
    time_execution_list.append((t2-t1)*1000)


    print('''
                Operaciones         Tiempo
        Caso1   {}                  {}
        Caso2   {}                  {}
        Caso3   {}                  {}
            '''.format(cant_operation_list[0],time_execution_list[0],
            cant_operation_list[1],time_execution_list[1],
            cant_operation_list[2],time_execution_list[2],))
    