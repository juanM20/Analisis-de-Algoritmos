import os
import sys

if __name__ == '__main__':
	inputFileList= []
	outputFileList= []

	if len(sys.argv)!=2:
		print("Faltan o sobran argumentos: [numero_de_archivos]")
	else:
		for i in range(0, int(sys.argv[1])):
			name= input("Nombre de archivo sin extension "+str(i+1)+": ")
			inputFileList.append(name+".txt")
			outputFileList.append(name+"Resultados")

	for i in range(0, len(inputFileList)):
		runCmd = "python LCS.py "+inputFileList[i]+" "+outputFileList[i]
		os.system(runCmd)

	print("Ejecución finalizada.")

