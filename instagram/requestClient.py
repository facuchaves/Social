import subprocess
import instagramConf
import time
import datetime
import requests
import json

secondsSleep = 60
cantPerRequest = 2000

gralHeader = {
		'cookie' : 'mid=WVUbwAAEAAGWQ6aSQDF34Qj1WsK_; datr=KUyXWTe2D4sLZeEUl2BqRmAV; sessionid=IGSC98b30633420150d385a972fbf1e34a93d759d75eb003bac27b90e498e92d3351%3AAbXt7SNycqzLo6P89g969mgJC6V1aXtN%3A%7B%22_auth_user_id%22%3A1457071243%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_token_ver%22%3A2%2C%22_token%22%3A%221457071243%3Ak1LsyysYGUql9M3kh8LyW2NAr2HudvDo%3A16c7cb8020504e34e13237d550bc569d776af55c5d1c1ac88ed61e3777d2f82a%22%2C%22_platform%22%3A4%2C%22last_refreshed%22%3A1514669180.461874485%2C%22asns%22%3A%7B%22time%22%3A1505737893%2C%22181.30.57.66%22%3A10318%7D%7D; ig_vw=1301; ig_pr=1; ig_vh=654; csrftoken=j4LxhOoeosYnVA41hrVyQQhSAJD1cMEN; rur=ATN; ds_user_id=1457071243; urlgen="{\"time\": 1514679745}:1eVROq:Jg7ym2ACQG295i0f3cMhCWSsw8g"' ,
		'origin' : 'https://www.instagram.com' ,
		'accept-encoding' : 'gzip, deflate, br' ,
		'accept-language' : 'en-US,en;q=0.8' ,
		'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' ,
		'x-requested-with' : 'XMLHttpRequest' ,
		'x-csrftoken' : 'j4LxhOoeosYnVA41hrVyQQhSAJD1cMEN' ,
		'x-instagram-ajax' : '1' ,
		'content-type' : 'application/x-www-form-urlencoded' ,
		'accept' : '*/*' ,
		'referer' : 'https://www.instagram.com/ana_kari_86/followers/?hl=en' ,
		'authority' : 'www.instagram.com' ,
		'content-length' : '0'
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
