import subprocess
import instagramConf
import time

secondsSleep = 3

def searchMysFollowings():
	searchFollowings(instagramConf.myId)

def searchFollowings(id):
	Process=subprocess.Popen('./searchFollowings.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def searchMysFollowers():
	searchFollowers(instagramConf.myId)

def searchFollowers(id):
	Process=subprocess.Popen('./searchFollowers.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def follow(id):
	print '\n'
	print 'Following : ' + str(id)
	Process=subprocess.Popen('./follow.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def unfollow(id):
	print '\n'
	print 'Unfollowing : ' + str(id)
	Process=subprocess.Popen('./unfollow.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)