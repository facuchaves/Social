import instagramService
import sys

import logs

f = open('instagram.log', 'a')
original = sys.stdout
sys.stdout = logs.Tee(sys.stdout, f)

instagramService.unfollowNonFollowersBack(True)

f.close()