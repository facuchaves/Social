import subprocess
import time

def search():
	Process=subprocess.Popen('./search.sh ', shell=True)
	time.sleep(5)

def like(id):
	Process=subprocess.Popen('./like.sh %s ' % (str(id),), shell=True)
	time.sleep(2)
