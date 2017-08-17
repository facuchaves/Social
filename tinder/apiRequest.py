import requests
import time

token = '797c7572-bec3-41b9-920c-46a89a2b7700'
gralHeader = {
		'Origin' : 'https://www.tinder.com',
		'Accept-Encoding' : 'gzip, deflate, br',
		'Accept-Language' : 'en-US,en;q=0.8',
		'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'Accept' : '*/*',
		'Referer' : 'https://www.tinder.com/',
		'x-auth-token' : token,
		'Connection' : 'keep-alive',
		'platform' : 'web',
		'app-version' : '1000000'
	}

def search():
	urlSearch = 'https://api.gotinder.com/recs/core?locale=en'

	headersSearch = gralHeader
	headersSearch['If-None-Match'] = 'W/"1958333664"'

	r = requests.get(urlSearch, headers=headersSearch)

	return r.json()

def like(id):
	urlLike = 'https://api.gotinder.com/like/' + id + '?locale=en'

	r = requests.get(urlLike, headers=gralHeader)
	print "Like : " + id
	print r.text
	time.sleep(2)

