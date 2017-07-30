import apiCurl

'''
Sigue los seguidores de un usuario
'''
def followFollowersByUserName(userName):
	print 'Siguiendo usuario de ' + str(userName)

	lines = getLinesAndRemoveFromFile('Datos/Ids_A_Seguir_De_' + str(userName) )
	for id in lines:
		apiCurl.follow( id )

def getLinesAndRemoveFromFile(fileName):
	lines = open(fileName).readlines()
	open(fileName, 'w').writelines(lines[1000 : len(lines) ])
	return lines[0 : 1000]

'''
Deja de seguir
'''
def unfollowNonFollowersBack():
	print 'Dejando de seguir no seguidores'
	with open('Datos/DejarDeSeguir') as unfollowers:
		for id in unfollowers:
			apiCurl.unfollow( id )


#unfollowNonFollowersBack()
followFollowersByUserName("Patro")