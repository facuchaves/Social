import subprocess
import instagramData
import time

secondsSleep = 7

def searchMysFollowings():
	searchFollowings(instagramData.myId)

def searchFollowings(id):
	Process=subprocess.Popen('./searchFollowings.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def searchMysFollowers():
	searchFollowers(instagramData.myId)

def searchFollowers(id):
	Process=subprocess.Popen('./searchFollowers.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def follow(id):
	print 'follow ' + str(id)
	Process=subprocess.Popen('./follow.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def unfollow(id):
	print 'unfollow ' + str(id)
	Process=subprocess.Popen('./unfollow.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)