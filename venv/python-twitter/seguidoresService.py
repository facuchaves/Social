'''
Funciones para seguir y dejar de seguir.
'''

import twitterApiClient
import procesamientoArchivos
import reporte
import threading
import time
import datetime
import seguidoresModel

listaDejarDeSeguir=[]
listaAChupar=[]
listaProcesados=[]
CONTADOR=0
TOPE_DIARIO=1#000

'''
DEJAR DE SEGUIR SECCION
'''

#Funcion que deja de seguir no-seguidores concurrentemente
def dejarDeSeguirConcurrente(flagActualizar):
	print 'Dejando de seguir no-seguidores ...'
	if flagActualizar:
		actualizarDejarDeSeguir()

	inicializarIdsDejarDeSeguir()

	print str( len( listaDejarDeSeguir ) ) + ' no-seguidores para dejar de seguir.'

	threadList = []

	global CONTADOR
	CONTADOR=0

	for x in xrange(0,1):
		threadList.append(threading.Thread( target=dejarDeSeguir ))

	for thread in threadList:
	    #thread.daemon = True
	    thread.start()
	    #time.sleep(5)

	for thread in threadList:
		#thread.daemon = True
		thread.join()

	reporte.generarReporte("Datos/DejarDeSeguir",listaProcesados,listaDejarDeSeguir)

#Funcion que deja de seguir no-seguidores
def dejarDeSeguir():
	global CONTADOR
	while (True):
		time.sleep(2)
		if CONTADOR > 0 and CONTADOR%10 == 0:
			print('Se dejaron de seguir ' + str(CONTADOR) + ' usuarios.')
		idDejarDeSeguir = obtenerSiguienteIdDejarDeSeguir()
		if idDejarDeSeguir == None:
			print('Se dejaron de seguir ' + str(CONTADOR) + ' usuarios.')
			break
		resp, content , aplicationName = twitterApiClient.dejarDeSeguir(idDejarDeSeguir )
		respuestaProcesado = seguidoresModel.RespuestaProcesado( datetime.datetime.now() , idDejarDeSeguir , resp , content , aplicationName )
		lock = threading.Lock()
		lock.acquire()
		#TODO Agregar logica que si tiene error, reportarlo, pero dejarlo en el archivo de dejar de seguir asi no se pierde y lo vuelve a intentar de dejar de seguir mas adelante
		listaProcesados.append(respuestaProcesado)
		CONTADOR += 1
		if 	'errors' in content:
			if ( content['errors'][0]['code'] == 161 ):#108: Usuario no encontrado.
				print 'No se puede dejar de seguir mas limite alcanzado.'
				lock.release()
				print('Se dejaron de seguir ' + str(CONTADOR) + ' usuarios.')
				break
			
			if ( content['errors'][0]['code'] == 89 ):#108: Usuario no encontrado.
				print 'No se puede dejar de seguir mas token expirado: ' + aplicationName
				lock.release()
				print('Se dejaron de seguir ' + str(CONTADOR) + ' usuarios.')
				break
		lock.release()
		
def inicializarIdsDejarDeSeguir():
	with open( "Datos/DejarDeSeguir", 'rU') as fileDejarDeSeguir:
		for idDejarDeSeguir in fileDejarDeSeguir:
			listaDejarDeSeguir.append(idDejarDeSeguir)
	fileDejarDeSeguir.close()

def obtenerSiguienteIdDejarDeSeguir():
	lock = threading.Lock()
	lock.acquire()
	idDejarDeSeguir =  None
	if listaDejarDeSeguir:
		idDejarDeSeguir = listaDejarDeSeguir.pop()
	lock.release()
	return idDejarDeSeguir

'''
SEGUIR USUARIOS SECCION
'''

#Funcion que chupa seguidores concurrentemente
def chuparSeguidoresConcurrente(fileName):
	print 'Siguiendo usuarios ...'
	inicializarIdsAChupar(fileName)

	threadList = []

	global CONTADOR
	CONTADOR=0

	for x in xrange(0,1):
		threadList.append(threading.Thread( target=chuparSeguidores ))

	for thread in threadList:
	    #thread.daemon = True
		thread.start()
		#time.sleep(1)

	for thread in threadList:
	    #thread.daemon = True
	    thread.join()

	reporte.generarReporte(fileName,listaProcesados,listaAChupar)

#Funcion que chupa seguidores
def chuparSeguidores():
	global CONTADOR
	global TOPE_DIARIO
	while (CONTADOR < TOPE_DIARIO):
		time.sleep(2)
		if CONTADOR > 0 and CONTADOR%10 == 0:
			print('Se siguieron ' + str(CONTADOR) + ' usuarios.')
		idSeguidorAChupar = obtenerSiguienteIdAChupar()
		if idSeguidorAChupar == None:
			print('Se siguieron ' + str(CONTADOR) + ' usuarios.')
			break
		resp, content , aplicationName = twitterApiClient.seguir(idSeguidorAChupar )
		respuestaProcesado = seguidoresModel.RespuestaProcesado( datetime.datetime.now() , idSeguidorAChupar , resp , content , aplicationName )
		lock = threading.Lock()
		lock.acquire()
		#TODO Agregar logica que si tiene error, reportarlo, pero dejarlo en el archivo de seguir asi no se pierde y lo vuelve a intentar de seguir mas adelante
		listaProcesados.append(respuestaProcesado)
		CONTADOR += 1
		if 	'errors' in content:
			if ( content['errors'][0]['code'] == 161 ):#108: Usuario no encontrado.
				print 'No se puede seguir mas, limite alcanzado'
				lock.release()
				print('Se siguieron ' + str(CONTADOR) + ' usuarios.')
				break
			if ( content['errors'][0]['code'] == 89 ):#108: Usuario no encontrado.
				print 'No se puede dejar de seguir mas token expirado: ' + aplicationName
				lock.release()
				print('Se siguieron ' + str(CONTADOR) + ' usuarios.')
				break
		lock.release()

def inicializarIdsAChupar(fileName):
	with open( fileName, 'rU') as fileChupar:
		for idSeguidorAChupar in fileChupar:
			listaAChupar.append(idSeguidorAChupar)
	fileChupar.close()

def obtenerSiguienteIdAChupar():
	lock = threading.Lock()
	lock.acquire()
	idSeguidorAChupar =  None
	if listaAChupar:
		idSeguidorAChupar = listaAChupar.pop()
	lock.release()
	return idSeguidorAChupar

'''
Manejo de datos
'''

miId=163064210
miName='FacuChavesOk'

#Actualiza el archivo de mis seguidos
def actualizarMisSeguidos():
	print 'Actualizando mis seguidos.'
	resp, content , aplicationName = twitterApiClient.obtenerSeguidosByUserId(miId)
	print 'Cantidad seguidos : ' + str( len(content['ids'] ) )
	actualizarIdsEnArchivos( content['ids'] , 'Datos/Seguidos_Por_FacuChavesOk' )

#Actualiza el archivo de mis seguidores
def actualizarMisSeguidores():
	print 'Actualizando mis seguidores.'
	resp, content , aplicationName = twitterApiClient.obtenerSeguidoresByUserId(miId)
	print 'Cantidad seguidores : ' + str( len(content['ids'] ) )
	actualizarIdsEnArchivos( content['ids'] , 'Datos/Seguidores_De__FacuChavesOk' )

#Actualiza archivo de ids.
def actualizarIdsEnArchivos(ids,fileName):
	f = open( fileName , 'w+')
	for id in ids:
		f.write(str(id)+'\n')
	f.close()

#Obtiene los seguidores del id pasado por parametro y genera un archivo con todos los ids.
def obtenerSeguidores(id,name):
	twitterApiClient.obtenerSeguidoresByUserId(id)
	procesamientoArchivos.disjuncion('Datos/Seguidos_Por_FacuChavesOk','Datos/Seguidores_De_'+str(name),'Datos/Ids_A_Seguir_De_'+str(name))

#Comparar con https://web.crowdfireapp.com/#/163064210-tw/nonFollowers
def actualizarDejarDeSeguir():
	print 'Actualizando datos dejar de seguir.'
	actualizarMisSeguidos()
	actualizarMisSeguidores()
	procesamientoArchivos.disjuncion('Datos/Seguidores_De_FacuChavesOk','Datos/Seguidos_Por_FacuChavesOk','Datos/DejarDeSeguir')

print 'Compilando seguidoresService.py'