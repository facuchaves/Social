import requestClient
import json
import instagramConf
import os.path
import datetime

otherPublic = set()
myPublic = set()
publicToFollow = set()
myFollowers = set()
myFollowings = set()
idsToUnfollow = set()

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getFollowings(id):
	print str(datetime.datetime.now()) + ' Obteniendo los que sigue ' + str(id).rstrip()
	followingsJson = requestClient.searchFollowings(id)
	
	listIds = set()
	putFollowingsIdsInList(listIds,followingsJson)
	
	has_next = followingsJson['data']['user']['edge_follow']['page_info']['has_next_page']
	after = followingsJson['data']['user']['edge_follow']['page_info']['end_cursor']
	while ( has_next ):
		followingsAfterJson = requestClient.searchFollowings(id,after)
		putFollowingsIdsInList(listIds,followingsAfterJson)
		has_next = followingsAfterJson['data']['user']['edge_follow']['page_info']['has_next_page']
		after = followingsAfterJson['data']['user']['edge_follow']['page_info']['end_cursor']
	
	print str(datetime.datetime.now()) + ' Sigue ' + str(len(listIds))
	return listIds

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getFollowers(id):
	print str(datetime.datetime.now()) + ' Obteniendo seguidores de ' + str(id).rstrip()
	followersJson = requestClient.searchFollowers(id)

	listIds = set()
	putFollowersIdsInList(listIds,followersJson)
	
	has_next = followersJson['data']['user']['edge_followed_by']['page_info']['has_next_page']
	after = followersJson['data']['user']['edge_followed_by']['page_info']['end_cursor']
	while ( has_next ):
		followersAfterJson = requestClient.searchFollowers(id,after)
		putFollowersIdsInList(listIds,followersAfterJson)
		if 'data' in followersAfterJson:
			has_next = followersAfterJson['data']['user']['edge_followed_by']['page_info']['has_next_page']
			after = followersAfterJson['data']['user']['edge_followed_by']['page_info']['end_cursor']

	print str(datetime.datetime.now()) + ' Lo siguen ' + str(len(listIds))
	return listIds

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getMysFollowings():
	print str(datetime.datetime.now()) + ' Obteniendo los que sigo'
	global myFollowings
	myFollowings = getFollowings(instagramConf.myId)
	#putFollowingsIdsInList(myFollowings,followingsJson)
	print str(datetime.datetime.now()) + ' Sigo ' + str(len(myFollowings))

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getMysFollowers():
	print str(datetime.datetime.now()) + ' Obteniendo seguidores'
	global myFollowers
	myFollowers = getFollowers(instagramConf.myId)
	#putFollowersIdsInList(myFollowers,followersJson)
	print str(datetime.datetime.now()) + ' Me siguen ' + str(len(myFollowers))

'''
Pone los ids de followers en una lista
'''
def putFollowersIdsInList(list,jsonIds):
	putIdsInList(list , jsonIds , 'edge_followed_by')

'''
Pone los ids de followings en una lista
'''
def putFollowingsIdsInList(list,jsonIds):
	putIdsInList(list , jsonIds , 'edge_follow')

'''
Pone los ids en una lista
'''
def putIdsInList(list , jsonIds , edgeType):
	if 'data' in jsonIds:
		for node in jsonIds['data']['user'][edgeType]['edges']:
			list.add( str(node['node']['id']) )
'''
Actualiza los ids de usuarios que sigo y no me siguen.
'''
def updateMyData():
	print str(datetime.datetime.now()) + ' Actualizando mi info'
	getMysFollowers()
	getMysFollowings()
	global idsToUnfollow
	idsToUnfollow = myFollowings - myFollowers
	print str(datetime.datetime.now()) + ' #noSeguidores ' + str(len(idsToUnfollow))
	global myPublic
	myPublic = myFollowings | myFollowers

'''
'''
def getIdsToFollowFromUser(user):
	global otherPublic 
	otherFollowings = getFollowings(user.idUsuario)
	print str(datetime.datetime.now()) + ' Followings de ' + str(user.nombre) + ' -> ' + str(len(otherFollowings))

	otherFollowers = getFollowers(user.idUsuario)
	print str(datetime.datetime.now()) + ' Followers de ' + str(user.nombre) + ' -> ' + str(len(otherFollowers))
	
	otherPublic = otherFollowings | otherFollowers
	print str(datetime.datetime.now()) + ' Public de ' + str(user.nombre) + ' -> ' + str(len(otherPublic))

	print str(datetime.datetime.now()) + ' Actualizo mi info'
	updateMyData()
	print str(datetime.datetime.now()) + ' mypublic ' + str(len(myPublic))
	publicToFollow = otherPublic - myPublic

	print str(datetime.datetime.now()) + ' Public to follow -> ' + str(len(publicToFollow))

	publicToFollowFileName = 'Data/Public_' + str(user.idUsuario) + "_" + str(user.nombre) + '_ToFollow'

	#Si ya existe lo vacio para empezar de 0.
	if os.path.isfile(publicToFollowFileName):
		open( publicToFollowFileName , 'w').close()

	publicToFollowFile = open(publicToFollowFileName , "w+")
	for id in publicToFollow:
		publicToFollowFile.write(str(id) + '\n')
	
	publicToFollowFile.close()

'''
Obtiene las X primeras lineas y las devuelve.
'''
def getLinesAndRemoveFromFile(fileName):
	lines = open(fileName).readlines()
	open(fileName, 'w').writelines(lines[instagramConf.maxOperationsPerTime: len(lines) ])
	return lines[0:instagramConf.maxOperationsPerTime]

'''
Deja de seguir de a 35 a los que no me siguen
'''
def unfollowNonFollowersBack(update=True):
	print str(datetime.datetime.now()) + ' Dejando de seguir no seguidores'
	if(update):
		updateMyData()

	for id in list(idsToUnfollow)[:instagramConf.maxOperationsPerTime]:
		responseStr = requestClient.unfollow( id )
		if responseStr == "Espera unos minutos antes de volver a intentarlo." or responseStr == "Please wait a few minutes before you try again."  :
			print str(datetime.datetime.now()) +  "Hay que esperar, dejo de mandar request"
			break
		jsonResponse = json.loads( responseStr )
		if jsonResponse['status'] != "ok":
			print str(datetime.datetime.now()) +  "Ocurrio un error"
			print str(datetime.datetime.now()) +  jsonResponse
			break
	print str(datetime.datetime.now()) +  "------------------------------------FIN--------------------------------------"

'''
Sigue de a 35 seguidores de una persona especificada por id
'''
def followFromUser(user):
	print str(datetime.datetime.now()) + ' Siguiendo usuario de ' + str(user.idUsuario) + ":" + str(user.nombre)
	lines = getLinesAndRemoveFromFile('Data/Public_' + str(user.idUsuario) + "_" + str(user.nombre) + '_ToFollow')
	for id in lines:
		responseStr = requestClient.follow( id )
		if responseStr == "Espera unos minutos antes de volver a intentarlo." or responseStr == "Please wait a few minutes before you try again."  :
			print str(datetime.datetime.now()) +  "Hay que esperar, dejo de mandar request"
			break
		jsonResponse = json.loads( responseStr )
		if jsonResponse['status'] != "ok":
			print str(datetime.datetime.now()) +  "Ocurrio un error"
			print str(datetime.datetime.now()) +  jsonResponse
			break
	print str(datetime.datetime.now()) +  "------------------------------------FIN--------------------------------------"


'''
Obtiene usuarios de una lista de urls (lugar/hashtag) en el ultimo mes y los guarda en un archivo
'''
def getPublicByUrl(urls):
	for url in urls:
		print str(datetime.datetime.now()) + ' Obteniendo personas de la url ' + str(url).rstrip()
		followingsJson = requestClient.searchFollowings(id)
		
		listIds = set()
		putFollowingsIdsInList(listIds,followingsJson)
		
		has_next = followingsJson['data']['user']['edge_follow']['page_info']['has_next_page']
		after = followingsJson['data']['user']['edge_follow']['page_info']['end_cursor']
		while ( has_next ):
			followingsAfterJson = requestClient.searchFollowings(id,after)
			putFollowingsIdsInList(listIds,followingsAfterJson)
			has_next = followingsAfterJson['data']['user']['edge_follow']['page_info']['has_next_page']
			after = followingsAfterJson['data']['user']['edge_follow']['page_info']['end_cursor']
	
		print str(datetime.datetime.now()) + ' Sigue ' + str(len(listIds))
		return listIds