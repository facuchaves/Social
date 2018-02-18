import requests
import time
import datetime
import re

facebook_token = ""
facebook_id =  "775373923"

gralHeader = {
		'Origin' : 'https://www.tinder.com',
		'Accept-Encoding' : 'gzip, deflate, br',
		'Accept-Language' : 'en-US,en;q=0.8',
		'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'Accept' : '*/*',
		'Referer' : 'https://www.tinder.com/',
		'Connection' : 'keep-alive',
		'platform' : 'web',
		'app-version' : '1000000'
	}

def search():
	urlSearch = 'https://api.gotinder.com/recs/core?locale=en'

	refreshTinderToken()
	headersSearch = gralHeader
	headersSearch['If-None-Match'] = 'W/"-1052943510"'

	r = requests.get(urlSearch, headers=headersSearch)

	return r.json()

def like(id):
	urlLike = 'https://api.gotinder.com/like/' + id + '?locale=en'
	refreshTinderToken()
	r = requests.get(urlLike, headers=gralHeader)
	print str(datetime.datetime.now()) + " Like : " + id
	print r.text
	time.sleep(10)

#Obtiene el nuevo token tinder
def refreshTinderToken():

	facebook_token = refreshFacebookToken()

	urlRefreshTinderToken = "https://api.gotinder.com/auth"

	#No se usa pero lo dejo por si lo pide a futuro
	headerRefreshTinderToken = {
		'user-agent' : 'Tinder/4.0.9 (iPhone; iOS 8.0.2; Scale/2.00)',
		'content-type' : 'application/json'
	}

	r = requests.post(urlRefreshTinderToken , data = {'facebook_token' : facebook_token, 'facebook_id' : facebook_id } )

	#Formas de obtener el token de tinder.
	#r.json()['token']
	#r.json()['user']['api_token']
	#print r.text
	gralHeader['x-auth-token'] = r.json()['token']


def refreshFacebookToken():

	urlRefreshFacebookToken = 'https://www.facebook.com/connect/ping?client_id=464891386855067&domain=www.tinder.com&origin=1&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter%2Fr%2FlY4eZXm_YWu.js%3Fversion%3D42%23cb%3Df3506b78ffa0f58%26domain%3Dwww.tinder.com%26origin%3Dhttps%253A%252F%252Fwww.tinder.com%252Ff1bb0a33bb9f30c%26relation%3Dparent&response_type=token%2Csigned_request%2Ccode&sdk=joey'
	headersRefreshFacebookToken = {
		'accept-encoding' : 'gzip, deflate',
		'accept-language' : 'en-US,en;q=0.8',
		'upgrade-insecure-requests' : '1',
		'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'referer' : 'https://www.tinder.com/',
		'authority' : 'www.facebook.com',
		'cookie' : 'datr=XRZIWnKbPSqM5GVabD7TR1ka; sb=ZhZIWrRwxKnlz3nM6KhwBQa8; pl=y; wd=1301x654; c_user=775373923; xs=29%3AHgYyBNJU84FA0A%3A2%3A1514673767%3A368%3A15936; fr=0dcV9DkkFJBSUsdFG.AWV_j7jrMadfCN3ImxbXf89FBME.BaSBZX.EO.AAA.0.0.BaSCVu.AWXq68ds'
	}

	r = requests.get(urlRefreshFacebookToken, headers = headersRefreshFacebookToken )

	facebook_token = regexFacebookToken(r.url)

	return facebook_token

def regexFacebookToken(url):
	patternWithAnd = '(?<=(access_token\=))(.*?)(?=\&)'
	
	if re.search( patternWithAnd , url ) :
		#print 'URL CON &'
		#print re.search(patternWithAnd, url).group(0)
		return re.search(patternWithAnd, url).group(0)
	else :
		#print 'URL SIN &'
		#print url[ url.index('access_token=') + len('access_token=') :]
		return url[ url.index('access_token=') + len('access_token=') :]
	
####### Intentos de refrescar token ########

'''
Refresh token
curl 'https://api.gotinder.com/v2/auth/login/facebook?locale=en' 
  'Referer: https://www.tinder.com/' 
  'Origin: https://www.tinder.com' 
  'content-type: application/json' 
  'platform: web' 
  'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' 
  'app-version: 1000000' --data-binary '{"token":"EAAGm0PX4ZCpsBABxvi0ZCtd6Eifixr1vullpZCYZAO1yZAyZBneTEJZAeVOHRIJX2XfmPKiy1odHmZClnCEQsi74CXjp2t8f7D3XZA6ZCGkVkmSw8KKgwDYJAWjErH6f9lCpRr8eYTZCTCrPooYZC4ZBZCZCB2knu7anQIESKZAXmoNxKwZBkagblvKYc2sHcFPOeXlZC2ZCiYoo3F3f0LRQQZDZD"}' --compressed ;
'''


#TODO Terminar esto
def refreshFacebookToken2():
	urlRefreshFacebookToken = 'https://www.facebook.com/v2.6/dialog/oauth/confirm?dpr=1' 
	headersRefreshFacebookToken = {
		'origin' : 'https://www.facebook.com' ,
		'accept-encoding' : 'gzip, deflate', 
		'accept-language' : 'en-US,en;q=0.8',
		'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'content-type' : 'application/x-www-form-urlencoded',
		'accept' : '*/*',
		'referer' : 'https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd',
		'authority' : 'www.facebook.com',
		'cookie' : 'datr=XRZIWnKbPSqM5GVabD7TR1ka; sb=ZhZIWrRwxKnlz3nM6KhwBQa8; c_user=775373923; xs=29%3AHgYyBNJU84FA0A%3A2%3A1514673767%3A368%3A15936; fr=0dcV9DkkFJBSUsdFG.AWXRKVJETmD6Z6hZityGuavSjIc.BaSBZX.EO.AAA.0.0.BaSBZm.AWU2mZG8; pl=y; wd=1301x654; act=1514674407451%2F3; presence=EDvF3EtimeF1514676267EuserFA2775373923A2EstateFDutF1514676267858CEchFDp_5f775373923F14CC'
	}
	dataRefreshFacebookToken = 'fb_dtsg=AQFVKVOzwSRM%3AAQHRI6c-Mvny&app_id=464891386855067&redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=page&access_token=&sdk=ios&from_post=1&encoded_state=%257B%2522challenge%2522%253A%2522IUUkEUqIGud332lfu%25252BMJhxL4Wlc%25253D%2522%252C%25220_auth_logger_id%2522%253A%252230F06532-A1B9-4B10-BB28-B29956C71AB1%2522%252C%2522com.facebook.sdk_client_state%2522%253Atrue%252C%25223_method%2522%253A%2522sfvc_auth%2522%257D&private=&login=&read=&write=&extended=&social_confirm=&confirm=&seen_scopes=&auth_type=rerequest&auth_token=&auth_nonce=&default_audience=friends&ref=Default&return_format=return_scopes%2Cdenied_scopes%2Csigned_request%2Caccess_token&domain=&sso_device=iphone-safari&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&tfp=&sheet_name=initial&__CONFIRM__=1&__user=775373923&__a=1&__dyn=7AzHK4HwBgDxyHAzGgnzEdoKEW8xdLFwxx-1lhE98nwgU6C7WUC3q2OUuwmEdUOdwJwSwIUaonwvoiwBx62q1lCK1twbC1nwpVHxC326U6OfwNx-22awpoydzEjG4821Urx69wyUa84S9xa9w&__req=8&__be=1&__pc=PHASED%3ADEFAULT&__rev=3551329&jazoest=26581708675867912211983827758658172827354994577118110121'

	r = requests.post(urlRefreshFacebookToken, data = dataRefreshFacebookToken)

	#print r.text[r.text.index('access_token='):]
	print r.text