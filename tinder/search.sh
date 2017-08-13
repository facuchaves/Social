    #!/bin/bash -l
    #$ -S /bin/bash
    #$ -N $2
	curl 'https://api.gotinder.com/recs/core?locale=en' -H 'Origin: https://tinder.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Accept: */*' -H 'Referer: https://tinder.com/' -H 'x-auth-token: e48905c6-b6c3-4970-a477-97e20d6ce307' -H 'If-None-Match: W/"751836700"' -H 'Connection: keep-alive' -H 'platform: web' -H 'app-version: 1000000' --compressed > search.json