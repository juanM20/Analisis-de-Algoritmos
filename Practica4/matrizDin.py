from random import randint
import sys
#import numpy

class Matriz:
	def __init__(self, nMatriz, rows, cols):
		self.id= nMatriz
		self.rows= rows
		self.cols= cols

	def getMatrixName(self):
		return "A"+str(self.id)

	def getID(self):
		return self.id

	def getRows(self):
		return self.rows

	def getCols(self):
		return self.cols

	def setValues(self, listVal):
		self.values= listVal

	def getValues(self):
		return self.values
	
	def showMatrix(self):
		print(self.getMatrixName()+"("+str(self.getRows())+" x "+str(self.getCols())+")")
		for i in range(len(self.values)):
			for j in range(len(self.values[i])):
				print(self.values[i][j], end='\t')
			print()
		

def printMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print(matrix[i][j], end='\t')
		print()

#Para matrices S y M
def getZeroMatrix(n):
	matrix= []
	for i in range(0, n):          # A for loop for row entries 
	    a =[] 
	    for j in range(0, n):      # A for loop for column entries 
	         a.append(0) 
	    matrix.append(a)

	return matrix


def makeTableP(mList):
	existingDim= len(mList)+1 #Validar aquí que al menos no haya más dimensiones que las que se debe
	verifDim=[]

	verifDim.append(mList[0].getRows())
	verifDim.append(mList[0].getCols())
	for i in range(1, len(mList)):
		toVerif= mList[i].getRows()
		if toVerif in verifDim:
			verifDim.append(mList[i].getCols())
		else:
			print("ERROR. Not correct sequence of dimensions.")
			break

	return verifDim

#l es la lingitud de la cadena, osea las columnas
#i avanza en diagonales, osea checa las filas (celda)
#j recorre también por diagonales, osea checa las columnas (celda)
#k recorre 
def matrixChainOrder(M, P, S):
	n= len(P)-1
	#print("n= "+str(n))
	for i in range(n):
		M[i][i]= 0
		S[i][i]= 0
	
	for l in range(1, n):
		#print("\n==================================================================================> l= "+str(l+1))
		for i in range(0, n-l):
			#print()
			#print("i= "+str(i+1))
			j= i+l
			#print("j= "+str(j+1))
			for k in range(i, j):
				#print("k= "+str(k+1))
				#print("M["+str(i+1)+","+str(k+1)+"] + M["+str(k+2)+","+str(j+1)+"] + P"+str(i)+" P"+str(k+1)+" P"+str(j+1))
				q= M[i][k] + M[k+1][j] + P[i]*P[k+1]*P[j+1]
				#print("q= "+str(q))
				
				if k==i:
					M[i][j]= q
					S[i][j]= k+1
				else:
					if q<M[i][j]:
						M[i][j]= q
						S[i][j]= k+1

def printOptimalParens(S, i, j):
	if i==j:
		print("A"+str(i))
	else:
		print("(")
		printOptimalParens(S, i, S[i][j])
		printOptimalParens(S, S[i][j]+1, j)
		print(")")



if __name__== '__main__':
	if len(sys.argv) != 2:
	    print("Faltan o sobran argumentos: [número_de_matrices]")
	else:
		mArray= [] #Arreglod e amtrices
		matrixV= [] #Valores de la matriz
		nMatrix= (int)(sys.argv[1]) #Número de matrices que se van a meter

		for i in range(0, nMatrix):
			matrixV=[]
			print("Matriz A"+str(i+1))
			r= int(input("\tFilas: "))
			c= int(input("\tColumnas: "))
			newMatrix= Matriz(i+1, r, c)

			# For user input 
			for i in range(r):          # A for loop for row entries 
			    a =[] 
			    for j in range(c):      # A for loop for column entries 
			         a.append(randint(0, 15)) 
			    matrixV.append(a)

			newMatrix.setValues(matrixV)
			mArray.append(newMatrix) #Matriz Ai(rxc)

			print()
		"""
		for i in range(0, len(mArray)):
			mArray[i].showMatrix()
			print()
		"""
		
		P = makeTableP(mArray)
		print("Tabla P: "+str(P))


		# For printing the matrix
		M= getZeroMatrix(len(P)-1)
		S= getZeroMatrix(len(P)-1)
		matrices= matrixChainOrder(M, P, S)

		
		print("\nTabla M:")
		printMatrix(M)
		print("\nTabla S:")
		printMatrix(S)
		print()
		

		#printOptimalParens(S, 0, 5)



