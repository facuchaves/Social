import instagramService
import instagramData
import sys
import logs

f = open('instagram.log', 'a')
original = sys.stdout
sys.stdout = logs.Tee(sys.stdout, f)

#currentUser = instagramData.userMatiFerrario
#currentUser = instagramData.userStephiLucero
#currentUser = instagramData.userVitabellashoes
currentUser = instagramData.userOlivashoes

instagramService.getIdsToFollowFromUser(currentUser)
#instagramService.followFromUser(currentUser)

f.close()
