import apiCurl
import seguidoresService
import time

userName= "Chachi"
cantidadAProcesarPorLlamada = 80

'''
Sigue los seguidores de un usuario
'''
def followFollowersByUserName():
	lines = getLinesAndRemoveFromFile('Datos/Ids_A_Seguir_De_' + str(userName) )
	for idASeguir in lines:
		time.sleep(45)
		apiCurl.follow( idASeguir )

'''
Obtiene las primeras 80 lineas de un archivo
'''
def getLinesAndRemoveFromFile(fileName):
	lines = open(fileName).readlines()
	open(fileName, 'w').writelines(lines[cantidadAProcesarPorLlamada : len(lines) ])
	return lines[0 : cantidadAProcesarPorLlamada]

'''
Dejar de seguir
'''
def dejarDeSeguirNoSeguidores():
	seguidoresService.actualizarDejarDeSeguir()

	lines = getLinesAndRemoveFromFile( "Datos/DejarDeSeguir" )

	for idAUnfollow in lines:
		time.sleep(45)
		apiCurl.unfollow( idAUnfollow )


#Obtiene los seguidores del id pasado por parametro y genera un archivo con todos los ids.
def obtenerSeguidores(id,name):
	apiCurl.obtenerSeguidoresByUserId(id)
	procesamientoArchivos.disjuncion('Datos/Seguidos_Por_FacuChavesOk','Datos/Seguidores_De_'+str(name),'Datos/Ids_A_Seguir_De_'+str(name))
