'''
Llama a los servicios de twitter para obtener lista de ids de seguidos y seguidores.
'''

import oauth2 as oauth
import json
import random

idMio=163064210
nameMio='FacuChavesOk'

listaApps=[]

#listaApps.append( ( 'Seguidores 1.0' , 'J4BETC0JRrY07P0XBri179pwz' , 'c2smmrQ7bfoZ1MqDf2Y6XO4uF1If7dQBgdiyXZD5vTu5VPIOus' , '163064210-yAeGqQZ53Of9YEZ9QdmBXuVQkPlGZoe5BmfSffVZ' , 'XJFRPJdxdyYCye6rCtP1jbGURKNyhk1BGONjWIMfPmMuH' ) )
listaApps.append( ( 'Seguidores 2.0' , 'JbO3JaXB7sOjHpGzTZrGnNRYE' , 'cKYZ6fyhQ6nD0YMXQp5wrZV8OeeIpAOCRA1S1gDOU2Z0H0gGcG' , '163064210-oifWAtl9JdNSau0LUQxziGeQRwzXx5gOcAikdvkK' , 'pdcoHaYk8KtoaqG4QDKFl3cGgirVTN6PU0ynqa2oN7eka' ) )
listaApps.append( ( 'Seguidores 3.0' , 'sgQUtggGf7X849MXvR78NPlnb' , 'sPNQOc9g7biEyrHVTFsfUnhLU1Hsx57X6DouYnF4csTRMrRx9A' , '163064210-SELA3qlPeB1lhFblMSQAtQnt7vHX4e09iz65KLyT' , 'wcz3CDXVS0pUNNV4UqqKVrrrb9aAA888iSwdhxq8i4Kxu' ) )
listaApps.append( ( 'Seguidores 4.0' , 'oVRoQGMVQ11rlN1IOdZtVdTZP' , 'PyonNEvW5eExL4p5593d7xZTcAFTsbIhwTRzcdLflEjYa1FZoc' , '163064210-kLiLjcquV23Nqf2hRH4oQxvuzj8OUQ5BqL4nTkQB' , 'mY1vezF5tZUu5FD6IcuxBQ6pLwHa20aaZoWp2dv6Nk08X' ) )
#listaApps.append( ( 'Seguidores 5.0' , 'DZMfvpnvONImtymXO6qcAutAw' , 'vhr8vkjStutmuegREoF2lqTkbk15dlNGycNUg2f8lZosOU2FJR' , '163064210-ZqylNWDJk6WC1VkSLrgoOOPqwibC6yMgtYtPCZB1' , 'HYOt3j0ItUusX66GUw5cGi5Bl5F8dr158nhkuIRJDLWe4' ) )
listaApps.append( ( 'Seguidores 6.0' , 'BiYcUaZZcqFERGAfquLAqzDfg' , '2tkrKGCcipRvfdvaw8DBLuudXALXK40Gkbf1TIDyRKvv7W2y3U' , '163064210-NhSmi82w8mr6PgQHxk3BvgaRU6w2TalIblMX39nq' , 'z1mgZ3Nn5zqDMuEEe7dythpzeqCXWpUvyQ7KO3kiEdidx' ) )
listaApps.append( ( 'Seguidores 7.0' , 'sPC6r48V9qDgSUhyWVkEoZSzv' , 'qvPnCFH7NMpnnf9q0WNLCneBHQ7W7IMOgp43pb5CCr9ZLGUq6X' , '163064210-n9TYEqP43T8XqFpTU1VYE5t1Kso9gYEnsBHyFUS8' , 'ouB2x7YQYPrWiKXfvZYaMqBF8a8avUVbI7jPXVJQ1XRJ5' ) )
listaApps.append( ( 'Seguidores 8.0' , 'cVzj8awrsKxwxxqm8BtfyeTJI' , 'ELaPGFgFWPNbEOrimB1TGYh89Mb4lCfArCthQh3TzvlUtu1hTY' , '163064210-U0q79ItdH8sqlSArLc4IYSu276a9lL5OIzYFekDN' , 'OD9IWsDH9Xl2QT9ht9FmgOtHzE9fSrkdj0pWRkixqjTHR' ) )
listaApps.append( ( 'Seguidores 9.0' , 'FWH3IinxO5WMWKuFNeLa2jxY7' , 'LYI469sUfUbSHES14OJTukYsIurrCZkCh36ZbfaL45qZPe1xWo' , '163064210-ngG47UBCmoA2AOqFdW4TLDM0HbxxTUWnaAHgnhC1' , 'z8A2JmlGN0zGE7xFqCceDIECWJotMkzy7jNzjXMM0x4ZL' ) )

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