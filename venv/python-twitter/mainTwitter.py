'''
Main de twitter
'''

import twitterServicios

#twitterServicios.obtenerSeguidores(955133202,'Patro',True)

#Comparar con https://web.crowdfireapp.com/#/163064210-tw/nonFollowers
#twitterServicios.dejarDeSeguirConcurrente(False)

twitterServicios.chuparSeguidoresConcurrente('Datos/Ids_A_Seguir_De_Patro')
