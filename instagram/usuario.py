'''
Entidad que representa un usuario
'''

class Usuario:
	#Ver de instanciar mejor estas cosas
	nombre = ''
	idUsuario = 0

	def __init__(self, nombre ,idUsuario):
		self.nombre = nombre
		self.idUsuario = idUsuario
