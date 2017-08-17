import apiRequest

def likesEveryone():	
	jsonResponse = apiRequest.search()
	if 'results' in jsonResponse:
		for result in jsonResponse['results']:
			currentUserId = result['user']['_id']
			apiRequest.like( currentUserId )
	else:
		print 'There are not results'

for x in range (150):
	likesEveryone()