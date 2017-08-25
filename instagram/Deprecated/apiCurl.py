import subprocess
import instagramConf
import time
import datetime
import requests
import json

def searchFollowings(id):
	Process=subprocess.Popen('./searchFollowings.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def searchFollowers(id):
	Process=subprocess.Popen('./searchFollowers.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def follow(id):
	print '\n'
	print str(datetime.datetime.now()) + ' Following : ' + str(id)
	Process=subprocess.Popen('./follow.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)

def unfollow(id):
	print '\n'
	print str(datetime.datetime.now()) + ' Unfollowing : ' + str(id)
	Process=subprocess.Popen('./unfollow.sh %s ' % (str(id),), shell=True)
	time.sleep(secondsSleep)
