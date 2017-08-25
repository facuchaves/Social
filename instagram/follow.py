import instagramService
import instagramData
import sys
import logs

f = open('instagram.log', 'a')
original = sys.stdout
sys.stdout = logs.Tee(sys.stdout, f)

currentUser = instagramData.userEzeGarcia

#instagramService.getIdsToFollowFromUser(currentUser)
instagramService.followFromUser(currentUser)

f.close()