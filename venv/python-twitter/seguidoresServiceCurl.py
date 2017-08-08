import apiCurl
import seguidoresService
import threading
import time

listaDejarDeSeguir = []
idsASeguir = []
TOPE_DIARIO=1000
CONTADOR=0

userName= "Patro"

'''
Aumenta el contador
'''
def aumentarContador():
	global CONTADOR
	lock = threading.Lock()
	lock.acquire()
	CONTADOR += 1
	lock.release()
'''
Sigue los seguidores de un usuario
'''
def followFollowersByUserName():
	print 'Siguiendo usuario de ' + str(userName)
	global TOPE_DIARIO
	global CONTADOR
	
	while (CONTADOR < TOPE_DIARIO):
		time.sleep(1)
		aumentarContador()
		idASeguir = obtenerSiguienteId(idsASeguir)
		if idASeguir == None:
			break
		apiCurl.follow( idASeguir )

def inicializarIdsASeguir():
	lines = getLinesAndRemoveFromFile('Datos/Ids_A_Seguir_De_' + str(userName) )
	for idASeguir in lines:
		idsASeguir.append(idASeguir)

'''
Obtiene las primeras 1000 lineas de un archivo
'''
def getLinesAndRemoveFromFile(fileName):
	lines = open(fileName).readlines()
	open(fileName, 'w').writelines(lines[1000 : len(lines) ])
	return lines[0 : 1000]

'''
Deja de seguir
'''
def unfollowNonFollowersBack():
	print 'Dejando de seguir no seguidores'
	while (True):
		time.sleep(1)
		idDejarDeSeguir = obtenerSiguienteId(listaDejarDeSeguir)
		if idDejarDeSeguir == None:
			break
		apiCurl.unfollow( idDejarDeSeguir )

def inicializarIdsDejarDeSeguir():
	with open( "Datos/DejarDeSeguir", 'rU') as fileDejarDeSeguir:
		for idDejarDeSeguir in fileDejarDeSeguir:
			listaDejarDeSeguir.append(idDejarDeSeguir)
	fileDejarDeSeguir.close()

'''
Devuelve el siguiente id de la lista pasada por parametro
Es Syncronizado
'''
def obtenerSiguienteId(listaAObtener):
	lock = threading.Lock()
	lock.acquire()
	idADevolver =  None
	if listaAObtener:
		idADevolver = listaAObtener.pop()
	lock.release()
	return idADevolver

def dejarDeSeguirConcurrente():
	print 'Actualizando dejar de seguir concurrente'
	seguidoresService.actualizarDejarDeSeguir()

	inicializarIdsDejarDeSeguir()

	print 'Dejando de seguir concurrente'
	ejecutarConcurrentemente(unfollowNonFollowersBack)

def seguirConcurrente():
	print 'Siguiendo concurrente'
	inicializarIdsASeguir()

	ejecutarConcurrentemente(followFollowersByUserName)

	print('Se siguieron ' + str(CONTADOR) + ' usuarios.')

def ejecutarConcurrentemente(targetMethod,cantidadHilos=1):
	threadList = []

	for x in xrange(0,cantidadHilos):
		threadList.append(threading.Thread( target=targetMethod ))

	for thread in threadList:
	    thread.start()

	for thread in threadList:
		thread.join()

#dejarDeSeguirConcurrente()
seguirConcurrente()