'''
Claves para el acceso a twitter
'''
import random

listaApps=[]

listaApps.append( 
	( 
		'Seguidores 1.0' , 
		'J4BETC0JRrY07P0XBri179pwz' , 
		'c2smmrQ7bfoZ1MqDf2Y6XO4uF1If7dQBgdiyXZD5vTu5VPIOus' , 
		'163064210-f8wdC6DNao9n8Jz7pWhb6DITeDr5PhqS9fQDjJfr' , 
		'3rT50Hl2GgKYqYdJpqQAXuPystXIwRoZzkoSIAiTH5n94' 
	)
)

listaApps.append( 
	( 
		'Seguidores 2.0' , 
		'JbO3JaXB7sOjHpGzTZrGnNRYE' , 
		'cKYZ6fyhQ6nD0YMXQp5wrZV8OeeIpAOCRA1S1gDOU2Z0H0gGcG' , 
		'163064210-oifWAtl9JdNSau0LUQxziGeQRwzXx5gOcAikdvkK' , 
		'pdcoHaYk8KtoaqG4QDKFl3cGgirVTN6PU0ynqa2oN7eka' 
	) 
)

listaApps.append( 
	( 
		'Seguidores 3.0' , 
		'sgQUtggGf7X849MXvR78NPlnb' , 
		'sPNQOc9g7biEyrHVTFsfUnhLU1Hsx57X6DouYnF4csTRMrRx9A' , 
		'163064210-PIIPMHPuEqi3ztoLCY3xUlasRhOZ8IDJJiJLuWFy' , 
		'iJpinJJiyf13y8pUVhllMWgMBxRci8RaCwW7UAn1UFn5b' 
	) 
)

listaApps.append( 
	( 
		'Seguidores 4.0' , 
		'oVRoQGMVQ11rlN1IOdZtVdTZP' , 
		'PyonNEvW5eExL4p5593d7xZTcAFTsbIhwTRzcdLflEjYa1FZoc' , 
		'163064210-kLiLjcquV23Nqf2hRH4oQxvuzj8OUQ5BqL4nTkQB' , 
		'mY1vezF5tZUu5FD6IcuxBQ6pLwHa20aaZoWp2dv6Nk08X' 
	) 
)
'''
listaApps.append( 
	( 
		'Seguidores 5.0' , 
		'DZMfvpnvONImtymXO6qcAutAw' , 
		'vhr8vkjStutmuegREoF2lqTkbk15dlNGycNUg2f8lZosOU2FJR' , 
		'163064210-nITLIXs9PU8Iz08Upwv0LOg23FECtXCyWIixyRxm' , 
		'U1RrwGIRWU24SBF2D2jYSHY1XbZeC7aCJtCUAZ63N05be' 
	) 
)
'''
listaApps.append( 
	( 
		'Seguidores 6.0' , 
		'BiYcUaZZcqFERGAfquLAqzDfg' , 
		'2tkrKGCcipRvfdvaw8DBLuudXALXK40Gkbf1TIDyRKvv7W2y3U' , 
		'163064210-NhSmi82w8mr6PgQHxk3BvgaRU6w2TalIblMX39nq' , 
		'z1mgZ3Nn5zqDMuEEe7dythpzeqCXWpUvyQ7KO3kiEdidx' 
	) 
)

listaApps.append( 
	( 
		'Seguidores 7.0' , 
		'sPC6r48V9qDgSUhyWVkEoZSzv' , 
		'qvPnCFH7NMpnnf9q0WNLCneBHQ7W7IMOgp43pb5CCr9ZLGUq6X' , 
		'163064210-n9TYEqP43T8XqFpTU1VYE5t1Kso9gYEnsBHyFUS8' , 
		'ouB2x7YQYPrWiKXfvZYaMqBF8a8avUVbI7jPXVJQ1XRJ5' 
	) 
)

listaApps.append( 
	( 
		'Seguidores 8.0' , 
		'cVzj8awrsKxwxxqm8BtfyeTJI' , 
		'ELaPGFgFWPNbEOrimB1TGYh89Mb4lCfArCthQh3TzvlUtu1hTY' , 
		'163064210-U0q79ItdH8sqlSArLc4IYSu276a9lL5OIzYFekDN' , 
		'OD9IWsDH9Xl2QT9ht9FmgOtHzE9fSrkdj0pWRkixqjTHR' 
	) 
)

listaApps.append( 
	( 
		'Seguidores 9.0' , 
		'FWH3IinxO5WMWKuFNeLa2jxY7' , 
		'LYI469sUfUbSHES14OJTukYsIurrCZkCh36ZbfaL45qZPe1xWo' , 
		'163064210-ngG47UBCmoA2AOqFdW4TLDM0HbxxTUWnaAHgnhC1' , 
		'z8A2JmlGN0zGE7xFqCceDIECWJotMkzy7jNzjXMM0x4ZL' 
	) 
)

listaApps.append( 
	( 
		'Seguidores 10.0' , 
		'eRafSnIEU2URaWnKk9D9tbRFt' , 
		'OI1by5sVonQdz21pJnOU2mqoadAXIIPMfChxIPkSyyOcxpV3y0' , 
		'163064210-NsFPGsq2zfOYYq2NZ26qX2D3O6IbhFP92hlKlWuw' , 
		'H79dNfirVFMjReh6GmqGbgydGVqJ6ZneFsQuqx7KoASxk' 
	) 
)

def obtenerRandomKey():
	index = random.randrange( len(listaApps)  )	
	return listaApps[index]

print 'Compilando keys.py'
