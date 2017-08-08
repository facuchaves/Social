import apiCurl
import json
import instagramConf
import os.path
import procesamientoArchivos

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getMysFollowings():
	print 'Obteniendo los que sigo'
	apiCurl.searchMysFollowings()
	followinsJsonToPlainId('Data/Followings_' + str(instagramConf.myId))

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getMysFollowers():
	print 'Obteniendo seguidores'
	apiCurl.searchMysFollowers()
	followersJsonToPlainId('Data/Followers_' + str(instagramConf.myId))

'''
Pasa de Json a texto plano con ids de los seguidores
'''
def followersJsonToPlainId(jsonFileName):
	jsonToPlainId(jsonFileName , 'edge_followed_by')

'''
Pasa de Json a texto plano con ids de los seguidos
'''
def followinsJsonToPlainId(jsonFileName):
	jsonToPlainId(jsonFileName , 'edge_follow')

'''
Pasa de un archivo .json a uno de ids planos
'''
def jsonToPlainId(jsonFileName , edgeType):
	#Si ya existe lo vacio para empezar de 0.
	if os.path.isfile(jsonFileName):
		open( jsonFileName , 'w').close()

	plainsIdsFile = open(jsonFileName , "w+")
	
	with open(jsonFileName + '.json') as jsonFile:
	    data = json.load(jsonFile)
	    for node in data['data']['user'][edgeType]['edges']:
	    	plainsIdsFile.write( str(node['node']['id']) + '\n' )

	plainsIdsFile.close()

'''
Actualiza los ids de usuarios que sigo y no me siguen.
'''
def updateNonFollowerBack():
	print 'Actualizando no seguidores'
	getMysFollowers()
	getMysFollowings()
	print 'Haciendo disjuncion de mis no seguidores'
	procesamientoArchivos.disjuncion('Data/Followers_' + str(instagramConf.myId),'Data/Followings_' + str(instagramConf.myId),'Data/IdsToUnFollow' )

'''
Obtiene las X primeras lineas y las devuelve.
'''
def getLinesAndRemoveFromFile(fileName):
	lines = open(fileName).readlines()
	open(fileName, 'w').writelines(lines[instagramConf.maxOperationsPerTime: len(lines) ])
	return lines[0:instagramConf.maxOperationsPerTime]

'''
Obtiene todos los ids a seguir de un usuario
'''
def getIdsToFollowFromUser(user):
	print 'Buscando Followings'
	apiCurl.searchFollowings(user.idUsuario)

def procesandoJsonToPlainText(user):
	print 'Pasando de Json a PlainId'
	followinsJsonToPlainId('Data/Followings_' + str(user.idUsuario) )
	
	print 'Haciendo disjuncion'
	procesamientoArchivos.disjuncion('Data/Followers_' + str(instagramConf.myId),'Data/Followings_' + str(user.idUsuario),'Data/Followings_' + str(user.idUsuario) + "_" + str(user.nombre) + '_ToFollow' )

'''
Deja de seguir de a 35 a los que no me siguen
'''
def unfollowNonFollowersBack(update=True):
	print 'Dejando de seguir no seguidores'
	if( update):
		updateNonFollowerBack()

	lines = getLinesAndRemoveFromFile('Data/IdsToUnFollow')
	for id in lines:
		apiCurl.unfollow( id )

'''
Sigue de a 35 seguidores de una persona especificada por id
'''
def followFromUser(user):
	print 'Siguiendo usuario de ' + str(user.idUsuario) + ":" + str(user.nombre)
	lines = getLinesAndRemoveFromFile('Data/Followings_' + str(user.idUsuario) + "_" + str(user.nombre) + '_ToFollow')
	for id in lines:
		apiCurl.follow( id )
