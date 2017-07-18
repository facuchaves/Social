'''
Llama a los servicios de twitter para obtener lista de ids de seguidos y seguidores.
'''

import oauth2 as oauth
import json
import time
import keys

#Crea un cliente con Keys aleatorias
def buildClient():
	applicationName,CONSUMER_KEY,CONSUMER_SECRET,KEY,SECRET = keys.obtenerRandomKey()
	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	token = oauth.Token(key=KEY, secret=SECRET)
	client = oauth.Client(consumer, token)

	return applicationName , client

#Funcion para llamar API de twitter con las keys.
def send(url, http_method="GET", post_body=""):
	applicationName , client = buildClient()
	resp, content = client.request( url, method=http_method, body=post_body)

	try:
		return json.loads(str(resp).replace("'","\"").replace(": u",": ").strip('\n')), json.loads(content) , applicationName
	except ValueError:
		print 'Respuesta con error : ' + str(resp).replace("'","\"").replace(": u",": ").strip('\n')

#Envia un request y si tiene next cursor vuelve a llamar
def sendWithNextCursor(url, http_method="GET", post_body=""):
	resp, content , applicationName = send(url,http_method, post_body)
	
	if	'next_cursor' in content:
		next_cursor = content['next_cursor']
		while next_cursor != 0:
			time.sleep(1)
			cursorParam='&cursor='+str(next_cursor)
			nextCursorResp, nextCursorContent , nextCursorApplicationName = send( url + cursorParam , http_method , post_body )

			resp = nextCursorResp

			content['ids'].extend( nextCursorContent['ids'] )

			applicationName = nextCursorApplicationName

			next_cursor = nextCursorContent['next_cursor']

	return resp, content , applicationName

#Busca los seguidos del usuario con id pasado por parametro
def obtenerSeguidosByUserId(id):
	return sendWithNextCursor( 'https://api.twitter.com/1.1/friends/ids.json?user_id=' + str(id) )

#Busca los seguidores del usuario con id pasado por parametro
def obtenerSeguidoresByUserId(id):
	return sendWithNextCursor( 'https://api.twitter.com/1.1/followers/ids.json?user_id=' + str(id) )

#Sigue a un determinado usuario
def seguir(id):
	return send('https://api.twitter.com/1.1/friendships/create.json?user_id='+(str(id).rstrip('\n')) ,http_method="POST")

#Sigue a un determinado usuario
def dejarDeSeguir(id):
	return send('https://api.twitter.com/1.1/friendships/destroy.json?user_id='+(str(id).rstrip('\n')) ,http_method="POST")

def mensajeDirecto(mensaje,id):
	return send("https://api.twitter.com/1.1/direct_messages/new.json?text=" + str(mensaje).rstrip('\n') + "&user_id=" + str(id).rstrip('\n'), http_method="POST")

print 'Compilando twitterApiClient.py'