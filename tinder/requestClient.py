import requests
import time
import datetime

'''
Refresh token
curl 'https://api.gotinder.com/v2/auth/login/facebook?locale=en' -H 'Origin: https://www.tinder.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'content-type: application/json' -H 'Accept: */*' -H 'Referer: https://www.tinder.com/' -H 'Connection: keep-alive' -H 'platform: web' -H 'app-version: 1000000' --data-binary '{"token":"EAAGm0PX4ZCpsBABX0PzwTJSZBPiff6X22Ye4DrpAvgkyxXvg8eN7l2dfHtpkThSjRAHwbOLCqQik9ZASNrAHWG6OPmk3jciZCfhnW6xcSd1bZBAmJExo51ZAkhpvZBM33PYvyiwFnYCwCsNZCSDSZBsjB1qlfa4TmUEXoRPd6xvykcWfkJxNGV2z6uCl17p5ySZAc8TxL1jzpp0gZDZD"}' --compressed
'''

token = '0a24e368-beda-4ff0-90e4-d586d27ef841'
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
	headersSearch['If-None-Match'] = 'W/"-1052943510"'

	r = requests.get(urlSearch, headers=headersSearch)

	return r.json()

def like(id):
	urlLike = 'https://api.gotinder.com/like/' + id + '?locale=en'

	r = requests.get(urlLike, headers=gralHeader)
	print str(datetime.datetime.now()) + " Like : " + id
	print r.text
	time.sleep(10)

