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


if __name__ == '__main__':

    m1 = Matrix('A1',30,35)
    m2 = Matrix('A2',35,15)
    m3 = Matrix('A3',15,5)
    m4 = Matrix('A4',5,10)
    m5 = Matrix('A5',10,20)
    m6 = Matrix('A6',20,25)

    matrix_array = [m1,m2,m3,m4,m5,m6]

    list1,list2 = get_lists(matrix_array)

    Suma = 0
    i = len(list1)-1
    cont = 0

    while(len(list1) > 1):

        Aj = list1[i]
        Ak_index = Search_Ak(Aj, list2)

        
