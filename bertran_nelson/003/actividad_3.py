class Persona():

	"""
	def __init__(self, nombre, apellido):
		pass
	"""
	def getNombre(self):
		return self.__nombre

	def setNombre(self, nombre):
		self.__nombre = nombre

	def getApellido(self):
		return self.__apellido

	def setApellido(self, apellido):
		self.__apellido = apellido

""" PRUEBA:
p1 = Persona()
p1.setNombre("NombreCualquiera")
p1.setApellido("ApellidoCualquiera")

print("p1 se llama: {} y su apellido es: {}".
	format(p1.getNombre(),p1.getApellido()))
"""