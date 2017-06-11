'''
Llama a los servicios de twitter para obtener lista de ids de seguidos y seguidores.
'''

import oauth2 as oauth
import json
import random
import time

idMio=163064210
nameMio='FacuChavesOk'

listaApps=[]

#Funcion para llamar API de twitter con las keys.
def oauth_req(url, applicationId = 0, http_method="GET", post_body="", http_headers="None" ):
	index = random.randrange( len(listaApps)  )	
	NAME,CONSUMER_KEY,CONSUMER_SECRET,KEY,SECRET = listaApps[index]
	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	token = oauth.Token(key=KEY, secret=SECRET)
	client = oauth.Client(consumer, token)
	resp, content = client.request( url, method=http_method, body=post_body)#, headers=http_headers)#, force_auth_header=True )
	return resp, content , NAME

'''
MOVER LA PARTE QUE ESCRIBE EN UN ARCHVO A TWITTERSERVICIOS.PY
'''
#Escribe en un archivo el resultado de llamar al servicio de twitter pasado por parametro
def obtenerIdsGenericos(url,fileName,reLlamar=True):
	content, idsGenericos , NAME = oauth_req( url , applicationId = 1 )
	data = json.loads(idsGenericos)
	#print content
	#print data
	#print idsGenericos
	if 	'next_cursor' in data:
		next_cursor = data['next_cursor']
		while reLlamar and next_cursor != 0:
			time.sleep(1)
			cursorParam='&cursor='+str(next_cursor)
			content, idsGenericos , NAME = oauth_req( url + cursorParam , applicationId = 1 )
			data2 = json.loads(idsGenericos)
			for id in data2['ids']:
				data['ids'].append(id)
			next_cursor = data2['next_cursor']
			print 'Obteniendo ' + str(len(data['ids'])) + ' elementos dentro del next_cursor para generar el archivo ' +  fileName
	
	if 	'ids' in data:
		f = open( fileName , 'w+')
		for id in data['ids']:
			f.write(str(id)+'\n')
		f.close()
	else:
		print 'No se encontraron ids para la llamada a la url: ' + url


#Escribe en un archivo los seguidos de un deteminado usuario.AGREAR QUE DEVUELVA EL NOMBRE DEL FILE
def obtenerSeguidos(id,name,full=True):
	url = 'https://api.twitter.com/1.1/friends/ids.json'
	url+='?user_id='+str(id)
	obtenerIdsGenericos(url,"Datos/Seguidos_Por_"+name,full)

#Escribe en un archivo los seguidores de un deteminado usuario.AGREAR QUE DEVUELVA EL NOMBRE DEL FILE
def obtenerSeguidores(id,name,full=True):
	url = 'https://api.twitter.com/1.1/followers/ids.json'
	url+='?user_id='+str(id)
	obtenerIdsGenericos(url,"Datos/Seguidores_De_"+name,full)

#Sigue a un determinado usuario
def seguir(id , applicationId = 0 ):
	url = 'https://api.twitter.com/1.1/friendships/create.json'
	url+='?user_id='+(str(id).rstrip('\n'))
	return oauth_req(url, applicationId , http_method="POST" )

#Sigue a un determinado usuario
def dejarDeSeguir(id , applicationId = 0 ):
	url = 'https://api.twitter.com/1.1/friendships/destroy.json'
	url+='?user_id='+(str(id).rstrip('\n'))
	return oauth_req(url, applicationId , http_method="POST" )

def mensajeDirecto(mensaje,id):
	url = "https://api.twitter.com/1.1/direct_messages/new.json"
	url += "?text=" + str(mensaje).rstrip('\n') + "&user_id=" + str(id).rstrip('\n')
	return oauth_req(url, applicationId = 0 , http_method="POST")

print 'Compilando twitterApiClient.py'