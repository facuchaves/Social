import os.path

#Funcion para obtener la disjuncion entre dos archivos.Obtiene solo los que esta en el file2 y no en el file1. OSEA FILE2-FILE1
def disjuncion(fileName1,fileName2,fileNameOutput):
	listaFile1 = []
	with open( fileName1, 'rU') as file1:
	  for elemFile1 in file1:
	     listaFile1.append(elemFile1)

	contador=0

	#Si ya existe lo vacio para empezar de 0.
	if os.path.isfile(fileNameOutput):
		open( fileNameOutput , 'w').close()

	outputFile = open(fileNameOutput , "w+")
	with open(fileName2, 'rU') as file2:
		for elemFile2 in file2:
			if elemFile2 not in listaFile1:
				outputFile.write(str(elemFile2))
				contador+=1
	outputFile.close()
	#print str(contador) + ' elementos que estan en ' + str(fileName2) + ' pero no en  ' + str(fileName1)
