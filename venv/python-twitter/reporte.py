'''
Genera archivos con el reporte de estado de los ids procesados y los pendientes de procesar.
'''

import os.path
import json
import datetime

#Genera un reporte en archivos de los ids procesados y de los ids que faltan procesar.
def generarReporte(fileName,listaProcesados,listaPendientes):
	generarReporteProcesadosProcesados(fileName,listaProcesados)
	generarReportePendientes(fileName,listaPendientes)


#Agregos todos los ids y la respuesta obtenida de los ids ya procesados a un archivo.
def generarReporteProcesadosProcesados(fileName,listaProcesados):
	print 'Generando Reporte de procesados.'
	if os.path.isfile(fileName+'_PROCESADOS'):
		fileProcesados = open(fileName+'_PROCESADOS','r+')
		content = fileProcesados.read()
		fileProcesados.seek(0,0)
		for tuplaRespuesta in reversed(listaProcesados):
			respJSON = json.loads(str(tuplaRespuesta[1]).replace("'","\"").strip('\n'))
			contentJSON = json.loads(str(tuplaRespuesta[2]).strip('\n'))
			status = respJSON['status']
			if 	'errors' in contentJSON:
				fileProcesados.write( str( datetime.datetime.now() ) + ' -> ' + str(tuplaRespuesta[0]).strip('\n') + " -> " + str(status).strip('\n') +  " -> " + str(contentJSON['errors']) + " -> " + str(tuplaRespuesta[3]).strip('\n') + "\n" )
			elif 'screen_name' in contentJSON:
				fileProcesados.write( str( datetime.datetime.now() ) + ' -> ' + str(tuplaRespuesta[0]).strip('\n') + " -> " + str(status).strip('\n') +  " -> " + str(contentJSON['screen_name']) + " -> " + str(tuplaRespuesta[3]).strip('\n') + "\n" )
			else:
				fileProcesados.write( str( datetime.datetime.now() ) + ' -> ' + str(tuplaRespuesta[0]).strip('\n') + " -> " + str(status).strip('\n') + " -> " + str(tuplaRespuesta[3]).strip('\n') + "\n" )
		fileProcesados.write(content)
		fileProcesados.close()
	else:
		fileProcesados = open(fileName+'_PROCESADOS','w+')
		for tuplaRespuesta in reversed(listaProcesados):
			respJSON = json.loads(str(tuplaRespuesta[1]).replace("'","\"").strip('\n'))
			contentJSON = json.loads(str(tuplaRespuesta[2]).strip('\n'))
			status = respJSON['status']
			if 	'errors' in contentJSON:
				fileProcesados.write( str( datetime.datetime.now() ) + ' -> ' + str(tuplaRespuesta[0]).strip('\n') + " -> " + str(status).strip('\n') +  " -> " + str(contentJSON['errors']) + " -> " + str(tuplaRespuesta[3]).strip('\n') +  "\n" )
			elif 'screen_name' in contentJSON:
				fileProcesados.write( str( datetime.datetime.now() ) + ' -> ' + str(tuplaRespuesta[0]).strip('\n') + " -> " + str(status).strip('\n') +  " -> " + str(contentJSON['screen_name']) + " -> " + str(tuplaRespuesta[3]).strip('\n') +  "\n" )
			else:
				fileProcesados.write( str( datetime.datetime.now() ) + ' -> ' + str(tuplaRespuesta[0]).strip('\n') + " -> " + str(status).strip('\n') + " -> " + str(tuplaRespuesta[3]).strip('\n') +  "\n" )
		fileProcesados.close()

#Piso el archivo original por un archivo solo con los pendientes, para que cuando se vuelve a procesar no vuelva a enviar solicitud a alguien que ya le envio anteriormente
def	generarReportePendientes(fileName,listaPendientes):
	print 'Generando Reporte de pendientes.'
	fileOriginal = open(fileName,'w+')
	for idPendiente in listaPendientes:
		fileOriginal.write(idPendiente)
	fileOriginal.close()

print 'Compilando reporte.py'