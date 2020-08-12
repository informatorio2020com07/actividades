class Persona():

	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def get_nombre(self):
		return self.nombre

	def get_apellido(self):
		return self.apellido

	def set_nombre(self,pnombre):
		self.nombre = pnombre
	
	def set_apellido(self, papellido):
		self.apellido = papellido
