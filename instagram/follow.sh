    #!/bin/bash -l
    #$ -S /bin/bash
    #$ -N $2
    echo >> instagramCurl.log
	echo $(date) >> instagramCurl.log
    echo 'follow' >> instagramCurl.log
    echo $1 >> instagramCurl.log
	curl "https://www.instagram.com/web/friendships/$1/follow/" -X POST -H 'cookie: mid=Vu2PFgAEAAGwnDnjEZufH02B2bMP; fbm_124024574287414=base_domain=.instagram.com; sessionid=IGSCfd3a10fa7e656fc06ec2a7671888a2ad16e7d98dfb540690fbcb2f031efd1de8%3Ayuray890owOV0f3E9LK3t76sj9A6I42D%3A%7B%22_auth_user_id%22%3A1457071243%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_token_ver%22%3A2%2C%22_token%22%3A%221457071243%3AmwsO5aC2TM5JwZ8rSJC4rN2ESJZbFdkg%3A359b9a494d4f7fbf3f927b4f690358124918608a35740c0d0aff370d7e3199ee%22%2C%22_platform%22%3A4%2C%22last_refreshed%22%3A1501352001.9799215794%2C%22asns%22%3A%7B%22time%22%3A1501352000%2C%22181.166.230.103%22%3A10318%7D%7D; ig_vw=1455; ig_pr=1.100000023841858; fbsr_124024574287414=AA73mBYVbcxL2nQtaJsNQTKhnf6Tb0_nj4Z039eKR7Q.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURFdDlhVWxQMDZiZUFDWHNhY1E5MmtMUDB1eEY1YU1IcDF3blI1dkdfREZzdlZ1TFhRQmlSSjVJeXUxWjYtbkRHb1EwcFlfWGQ2d0M5S29NUm9GT0xZcDZBb2VoSlF2eDg5MFBPUjJrSEtmdjBzMVpfVWNtY2FZZXVCbnRzZmZoR1NZRTd2TjhXekdSZ1hKdUxpRnhiQkNqeEE0SjRiaURIcjlwU01nX3JvSV9LTE5zWXlGN1ZiNkQyVjgzcExIOGlZMDl5Qjc3dlJBSWIwTmN6cVQzMEpweTRUZFNNU2ZlOEt3eE1mRzZ1d2w1X2c2dWV4bDJLZ0FlaXJHTk93UWlPWGFoUTNiVlc4Q1B5ckQtYjFfa1ZiY0Jja2VGckhHUHREUHBsbTAwcTdVcWJrblB3VE9SVnNLeWQ5WGF6bXAzRGVyOUZoNnRBN1VjSEtvVklVQWVyMyIsImlzc3VlZF9hdCI6MTUwMTM2MDk0MCwidXNlcl9pZCI6Ijc3NTM3MzkyMyJ9; rur=ASH; csrftoken=tPXqzjTO9knyqWa3vHAjjTy2AAJmJQHt; ds_user_id=1457071243' -H 'origin: https://www.instagram.com' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: es-ES,es;q=0.8' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36' -H 'x-requested-with: XMLHttpRequest' -H 'x-csrftoken: tPXqzjTO9knyqWa3vHAjjTy2AAJmJQHt' -H 'x-instagram-ajax: 1' -H 'content-type: application/x-www-form-urlencoded' -H 'accept: */*' -H 'referer: https://www.instagram.com/lautolosa/following/' -H 'authority: www.instagram.com' -H 'content-length: 0' --compressed >> instagramCurl.log