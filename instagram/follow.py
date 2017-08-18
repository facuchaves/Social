import instagramService
import instagramData
import sys

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

f = open('instagram.log', 'a')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)

currentUser = instagramData.userAgusNunez

#instagramService.getIdsToFollowFromUser(currentUser)
#instagramService.procesandoJsonToPlainText(currentUser)
instagramService.followFromUser(currentUser)

f.close()