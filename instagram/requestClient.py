import subprocess
import instagramConf
import time
import datetime
import requests
import json

secondsSleep = 60
secondsSleepGetFollowings = 2
cantPerRequest = 2000

''' 
#FacuChaves
gralHeader = {
		'cookie' : '7C35A40E-93FF-48FF-94D7-8E749DC9CDE1; mid=XkbqagAEAAGw-1KSKHb88SJ4rYMf; rur=FRC; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=MdIyNjZ6JPphIoKb3puhOYS5bjI4AyhE2fJCGeVBN_Y.eyJ1c2VyX2lkIjoiNzc1MzczOTIzIiwiY29kZSI6IkFRRGx2SXdteEFkY0QzZXdPR2JoLV84UFhVaC10ZWF0Zk42VURubVRiemRnVlVFRXllWF9wNTl6WGJzUXJRdFl0LXdMY1VwaFdiWThMRUNHTjg4NmtBSE5nQjlzd0JremhfS2ZIZUt3NVN6TEc5Z1lscVpSTk1aZFhrMmM4ZGxwRFlwQ2dCcjRHS1Y1VEhlOHNjcUZJT0lIcXZmY3Z3TXZ0YmpRRnh6SHZvZWs2ckJYcGczNi1uYkZ0Zkpsa3N2cV8tdTRwOGxkS2JCUG9MMzZ6eEpaTmd3TUg3aVNNSHpxNGo2a1NGVUtHWkswQ2dJVllZY3lJb0xvWnlaMXVBWEhEank1d19TZmE1RFdOaldtS3lDanRvUkdGcllTZlpaWW04dmRIcTk5b2lWM05lamNnU2R2SGlhZy1ncFJ1QVJLM2lnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdTYWNwQ2FzZDRRdFlTVUdQellNMkNpTkF1SkR3S1d2TklWd3BXRTNldVQ1aDZUeVRGaDN3eGJDbm52eXl0c0Y1RVBWYW92YXZ6S3NBdTdaQWxzQzdlelJvczVXeGxGOVpBZnZqN0c5dEo5R1JieVdTMGpXQ2J3ckoyQ1pBNnRITW9mdXZQSFA3cW1nTEk1QVpCWkJmNUNFSnMyZGJ3WkRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNTg3MTg1NzE3fQ; csrftoken=yXvHynNT7QMwhsC0bt91Pl8OL2LaP3Ws; ds_user_id=1457071243; sessionid=1457071243%3Aj0HAxx1ITYOSKj%3A28; shbid=3839; shbts=1588724297.8622239; urlgen="{\"190.191.58.64\": 10481}:1jW7lf:bMNhythYgPEMEaJnC-8ehJZEm7U"' ,
		'referer' : 'https://www.instagram.com' ,
		'origin' : 'https://www.instagram.com' ,
		'x-ig-app-id' : '936619743392459',
		'x-ig-www-claim' : 'hmac.AR2oSceKizKpu1ILfaMs4tK1SOXEokaxIbwtJQEOyuFxSUMk',
		'accept-encoding' : 'gzip, deflate, br' ,
		'accept-language' : 'en-US,en;q=0.8' ,
		'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' ,
		'accept' : '*/*' ,
		'authority' : 'www.instagram.com' ,
		'x-requested-with' : 'XMLHttpRequest',
		'x-csrftoken': 'yXvHynNT7QMwhsC0bt91Pl8OL2LaP3Ws',
		'x-instagram-ajax': 'c86f62fe51e1',
		'content-type': 'application/x-www-form-urlencoded',
		'content-length': '0'
	}
'''

#EzeBotta
gralHeader = {
		'cookie': 'ig_did=48A155CD-FCAF-463D-80BA-8E7F0A353F4D; mid=XrH-9gAEAAH2Sj9oGgdMpOYNUDAc; csrftoken=JzimUikLsMdeeT6zGkpIPhqjncfrHKEh; ds_user_id=34573408510; sessionid=34573408510%3AP2Zl0hwCC2ynBy%3A4; shbid=2075; shbts=1588723461.6767938; rur=ASH; urlgen="{\"190.191.58.64\": 10481}:1jW7yV:dS-FFdtDEBIDm2DWt5WZNjV-i4I"',
		'origin': 'https://www.instagram.com',
		'x-ig-www-claim': 'hmac.AR03Fl6CSkjdyCuQFXsLPoTBbpbbStOUGpdxTqm7EY4zAKUA',
		'accept-language': 'en-US,en;q=0.9',
		'x-requested-with': 'XMLHttpRequest',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
		'accept-encoding': 'gzip, deflate, br',
		'x-csrftoken': 'JzimUikLsMdeeT6zGkpIPhqjncfrHKEh',
		'x-ig-app-id': '936619743392459',
		'x-instagram-ajax': 'c86f62fe51e1',
		'content-type': 'application/x-www-form-urlencoded',
		'accept': '*/*',
		'referer': 'https://www.instagram.com/jor_rovitto/',
		'authority': 'www.instagram.com',
		'content-length': '0' 
	}

gralCookies = requests.cookies.RequestsCookieJar()
gralCookies.set('tasty_cookie', 'yum')

def follow(id):
	print str(datetime.datetime.now()) + ' Following : ' + str(id).rstrip()
	urlFollow = 'https://www.instagram.com/web/friendships/' + str(id).rstrip() + '/follow/?hl=en'
	r = requests.post(str(urlFollow), headers = gralHeader)
	print r.text
	time.sleep(secondsSleep)
	return r.text

def unfollow(id):
	#print str(datetime.datetime.now()) + ' Unfollowing : ' + str(id)
	urlUnfollow = "https://www.instagram.com/web/friendships/" + str(id).rstrip() + "/unfollow/"
	r = requests.post(urlUnfollow, headers=gralHeader)
	print r.text
	time.sleep(secondsSleep)
	return r.text

def searchFollowings(id,after = ""):
	#print str(datetime.datetime.now()) + ' Searching followins : ' + str(id)
	urlFollowings = "https://www.instagram.com/graphql/query/?query_id=17874545323001329&variables=%7B%22id%22%3A%22" + str(id).rstrip() + "%22%2C%22first%22%3A" + str(cantPerRequest)
	
	if ( after == "" ):
		urlFollowings += "%7D"
	else :
		urlFollowings += "%2C%22after%22%3A%22" + str(after) + "%22%7D"

	#print urlFollowings
	r = requests.get(urlFollowings, headers=gralHeader)
	#print r.text
	time.sleep(secondsSleepGetFollowings)
	return r.json()

def searchFollowers(id, after = ""):
	print str(datetime.datetime.now()) + ' Searching followers : ' + str(id)
	urlFollowers = "https://www.instagram.com/graphql/query/?query_id=17851374694183129&variables=%7B%22id%22%3A%22" + str(id).rstrip() + "%22%2C%22first%22%3A" + str(cantPerRequest)

	if ( after == "" ):
		urlFollowers += "%7D"
	else :
		urlFollowers += "%2C%22after%22%3A%22" + str(after) + "%22%7D"
	
	#print urlFollowers
	r = requests.get(urlFollowers, headers=gralHeader)
	#print r.text
	return r.json()

def searchMysFollowings():
	return searchFollowings(instagramConf.myId)

def searchMysFollowers():
	return searchFollowers(instagramConf.myId)
