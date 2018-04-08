'''
Genera archivos con el reporte de estado de los ids procesados y los pendientes de procesar.
'''

import os.path
import json
import seguidoresModel

#Genera un reporte en archivos de los ids procesados y de los ids que faltan procesar.
def generarReporte(fileName,listaProcesados,listaPendientes):
	generarReporteProcesadosProcesados(fileName,listaProcesados)
	generarReportePendientes(fileName,listaPendientes)


#Agregos todos los ids y la respuesta obtenida de los ids ya procesados a un archivo.
def generarReporteProcesadosProcesados(fileName,listaProcesados):
	print 'Generando Reporte de procesados.'
	print 'Se escribio en archivo ' + fileName + '_PROCESADOS'
	if os.path.isfile(fileName+'_PROCESADOS'):
		fileProcesados = open(fileName+'_PROCESADOS','r+')
		content = fileProcesados.read()
		fileProcesados.seek(0,0)
		
		for respuestaProcesado in reversed(listaProcesados):
			fileProcesados.write( respuestaProcesado.toString() )
		
		fileProcesados.write(content)
		fileProcesados.close()
	else:
		fileProcesados = open(fileName+'_PROCESADOS','w+')

		for respuestaProcesado in reversed(listaProcesados):
			fileProcesados.write( respuestaProcesado.toString() )

		fileProcesados.close()

#Piso el archivo original por un archivo solo con los pendientes, para que cuando se vuelve a procesar no vuelva a enviar solicitud a alguien que ya le envio anteriormente
def	generarReportePendientes(fileName,listaPendientes):
	print 'Generando Reporte de pendientes.'
	print 'Se escribio en archivo ' + fileName
	fileOriginal = open(fileName,'w+')
	for idPendiente in listaPendientes:
		fileOriginal.write(idPendiente)
	fileOriginal.close()

print 'Compilando reporte.py'