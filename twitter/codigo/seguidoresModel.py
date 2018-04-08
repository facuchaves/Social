'''
Entidad que tiene info de las respuestas
'''

class RespuestaProcesado:
	#Ver de instanciar mejor estas cosas
	fechaYHora = ''
	idUsuario = 0
	respuesta = ''
	content = ''
	aplicationName = ''

	def __init__(self, fechaYHora ,idUsuario ,respuesta ,content ,aplicationName ):
		self.fechaYHora = fechaYHora
		self.idUsuario = idUsuario
		self.respuesta = respuesta
		self.content = content
		self.aplicationName = aplicationName

	def toString(self):
		toString = str( self.fechaYHora ) + ' -> '
		toString += str( self.idUsuario ).strip('\n') + " -> "
		toString += str( self.respuesta['status'] ).strip('\n') + " -> " 
		
		if 	'errors' in self.content:
			toString += str( self.content['errors'] ) + " -> "
		
		elif 'screen_name' in self.content:
			toString += str( self.content['screen_name'] ) + " -> "

		toString += str( self.aplicationName ).strip('\n') + "\n"

		return toString

print 'Compilando RespuestaProcesado'