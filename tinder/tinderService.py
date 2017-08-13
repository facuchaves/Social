import apiCurl
import json
import time

def likesEveryone():	
		
	apiCurl.search()

	with open('search.json') as jsonFile:
		data = json.load(jsonFile)
		if 'results' in data:
			for result in data['results']:
				currentUserId = result['user']['_id']
				print '\n'
				print "Like : " + currentUserId
				apiCurl.like( currentUserId )
		else:
			print 'There are not results'

for x in range (15):
	likesEveryone()