'''
Funciones para seguir y dejar de seguir.
'''

import twitterApiClient
import procesamientoArchivos
import reporte
import threading
import json
import time
import datetime

idMio=163064210
nameMio='FacuChavesOk'

listaDejarDeSeguir=[]
listaAChupar=[]
listaProcesados=[]
CONTADOR=0
TOPE_DIARIO=1000

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
		resp, content , NAME = twitterApiClient.dejarDeSeguir(idDejarDeSeguir )
		tuplaRespuesta = (idDejarDeSeguir,resp,content , NAME )
		lock = threading.Lock()
		lock.acquire()
		#TODO Agregar logica que si tiene error, reportarlo, pero dejarlo en el archivo de dejar de seguir asi no se pierde y lo vuelve a intentar de dejar de seguir mas adelante
		listaProcesados.append(tuplaRespuesta)
		CONTADOR += 1
		contentJson = json.loads( str( content ) )
		if 	'errors' in contentJson:
			if ( contentJson['errors'][0]['code'] == 161 ):#108: Usuario no encontrado.
				print 'No se puede dejar de seguir mas limite alcanzado.'
				lock.release()
				print('Se dejaron de seguir ' + str(CONTADOR) + ' usuarios.')
				break
			
			if ( contentJson['errors'][0]['code'] == 89 ):#108: Usuario no encontrado.
				print 'No se puede dejar de seguir mas token expirado: ' + NAME
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
		time.sleep(1)
		if CONTADOR > 0 and CONTADOR%10 == 0:
			print('Se siguieron ' + str(CONTADOR) + ' usuarios.')
		idSeguidorAChupar = obtenerSiguienteIdAChupar()
		if idSeguidorAChupar == None:
			print('Se siguieron ' + str(CONTADOR) + ' usuarios.')
			break
		resp, content , NAME = twitterApiClient.seguir(idSeguidorAChupar )
		tuplaRespuesta = (idSeguidorAChupar,resp,content, NAME )
		lock = threading.Lock()
		lock.acquire()
		#TODO Agregar logica que si tiene error, reportarlo, pero dejarlo en el archivo de seguir asi no se pierde y lo vuelve a intentar de seguir mas adelante
		listaProcesados.append(tuplaRespuesta)
		CONTADOR += 1
		contentJson = json.loads( str( content ) )
		if 	'errors' in contentJson:
			if ( contentJson['errors'][0]['code'] == 161 ):#108: Usuario no encontrado.
				print 'No se puede seguir mas, limite alcanzado'
				lock.release()
				print('Se siguieron ' + str(CONTADOR) + ' usuarios.')
				break
			if ( contentJson['errors'][0]['code'] == 89 ):#108: Usuario no encontrado.
				print 'No se puede dejar de seguir mas token expirado: ' + NAME
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
FUNCIONES AUXILIARES
'''

def actulizarDatosMios():
	print 'Actualizando datos mios.'
	twitterApiClient.obtenerSeguidos(idMio,nameMio,True)
	twitterApiClient.obtenerSeguidores(idMio,nameMio,True)

#Obtiene los seguidores del id pasado por parametro y genera un archivo con todos los ids.
def obtenerSeguidores(id,name):
	twitterApiClient.obtenerSeguidores(id,name)
	procesamientoArchivos.disjuncion('Datos/Seguidos_Por_FacuChavesOk','Datos/Seguidores_De_'+str(name),'Datos/Ids_A_Seguir_De_'+str(name))

#Comparar con https://web.crowdfireapp.com/#/163064210-tw/nonFollowers
def actualizarDejarDeSeguir():
	print 'Actualizando datos dejar de seguir.'
	actulizarDatosMios()
	procesamientoArchivos.disjuncion('Datos/Seguidores_De_FacuChavesOk','Datos/Seguidos_Por_FacuChavesOk','Datos/DejarDeSeguir')

#Devuelve el id de una aplicacion para usar en las llamadas de chupar seguidores y de dejar de seguir
def getApplicationId():
	global APPLICATIONID
	lock = threading.Lock()
	lock.acquire()
	applicationIdADevolver =  APPLICATIONID
	APPLICATIONID += 1
	lock.release()
	print 'applicationId devuelto : ' + str(applicationIdADevolver)
	return applicationIdADevolver

print 'Compilando twitterServicios.py'