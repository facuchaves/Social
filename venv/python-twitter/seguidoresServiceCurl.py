import apiCurl
import seguidoresService
import time

userName= "Patro"
cantidadAProcesarPorLlamada = 80

'''
Sigue los seguidores de un usuario
'''
def followFollowersByUserName():
	lines = getLinesAndRemoveFromFile('Datos/Ids_A_Seguir_De_' + str(userName) )
	for idASeguir in lines:
		time.sleep(5)
		apiCurl.follow( idASeguir )

'''
Obtiene las primeras 80 lineas de un archivo
'''
def getLinesAndRemoveFromFile(fileName):
	lines = open(fileName).readlines()
	open(fileName, 'w').writelines(lines[cantidadAProcesarPorLlamada : len(lines) ])
	return lines[0 : cantidadAProcesarPorLlamada]

def dejarDeSeguirNoSeguidores():
	seguidoresService.actualizarDejarDeSeguir()

	lines = getLinesAndRemoveFromFile( "Datos/DejarDeSeguir" )

	for idAUnfollow in lines:
		time.sleep(5)
		apiCurl.unfollow( idAUnfollow )
	