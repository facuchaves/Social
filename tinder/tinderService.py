import apiRequest
import sys

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush() # If you want the output to be visible immediately
    def flush(self) :
        for f in self.files:
            f.flush()

f = open('tinder.log', 'a')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)

def likesEveryone():	
	jsonResponse = apiRequest.search()
	if 'results' in jsonResponse:
		for result in jsonResponse['results']:
			currentUserId = result['user']['_id']
			apiRequest.like( currentUserId )
	elif jsonResponse['status'] != 200:
		print 'Problemas con el token'
		print jsonResponse
	else:
		print 'There are not results'
		print jsonResponse

for x in range (15):
	likesEveryone()

f.close()