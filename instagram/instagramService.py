import apiCurl
import json
import instagramData
import os.path
import procesamientoArchivos

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getMysFollowings():
	print 'Obteniendo los que sigo'
	apiCurl.searchMysFollowings()
	followinsJsonToPlainId('Data/Followings_' + str(instagramData.myId))

'''
Obtiene los seguidos y los pasa de json a ids planos
'''
def getMysFollowers():
	print 'Obteniendo seguidores'
	apiCurl.searchMysFollowers()
	followersJsonToPlainId('Data/Followers_' + str(instagramData.myId))


def followersJsonToPlainId(jsonFileName):
	jsonToPlainId(jsonFileName , 'edge_followed_by')

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
	procesamientoArchivos.disjuncion('Data/Followers_' + str(instagramData.myId),'Data/Followings_' + str(instagramData.myId),'Data/IdsToUnFollow' )

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

def getLinesAndRemoveFromFile(fileName):
	lines = open(fileName).readlines()
	open(fileName, 'w').writelines(lines[instagramData.maxOperationsPerTime: len(lines) ])
	return lines

'''
Obtiene todos los ids a seguir de un usuario
'''
def getIdsToFollowFromUserId(userId):
	apiCurl.searchFollowings(userId)
	jsonToPlainId('Data/Followings_' + str(userId))
	procesamientoArchivos.disjuncion('Data/Followers_' + str(instagramData.myId),'Data/Followings_' + str(userId),'Followings_' + str(userId) + '_ToFollow' )

'''
Sigue de a 35 seguidores de una persona especificada por id
'''
def followFromUserId(userId):
	print 'Siguiendo usuario de ' + str(userId)
	with open('Data/Followings_' + str(userId) + '.json') as data_file:    
	    data = json.load(data_file)
	    #for node in data['data']['user']['edge_follow']['edges']:
	    	#print node['node']['id']
	    	#apiCurl.follow(id)
