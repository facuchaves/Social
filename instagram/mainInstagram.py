import instagramService
import instagramData

currentUser = instagramData.userAgusNunez

#instagramService.updateNonFollowerBack()
#instagramService.getIdsToFollowFromUser(currentUser)
#instagramService.procesandoJsonToPlainText(currentUser)
#instagramService.unfollowNonFollowersBack(False)
instagramService.followFromUser(currentUser)
