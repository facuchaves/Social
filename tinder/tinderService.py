import requestClient
import sys
import datetime
import time

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
	jsonResponse = requestClient.search()
	if 'results' in jsonResponse:
		for result in jsonResponse['results']:
			currentUserId = result['user']['_id']
			requestClient.like( currentUserId )
		return True
	if 'status' in jsonResponse and jsonResponse['status'] != 200:
		print str(datetime.datetime.now()) + ' Problemas con el token'
		print jsonResponse
		return False
	
	else:
		print str(datetime.datetime.now()) + ' No hay resultados'
		print jsonResponse
		return False

for x in range (15):
	continues = likesEveryone()
	if ( not continues ):
		break
	time.sleep(60)
print "------------------------------------FIN---------------------------------------------"

f.close()