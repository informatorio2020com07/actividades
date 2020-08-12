#Crear una clase Persona, que tenga atributo nombre y apellido, y los metodos get y set para cada atributo.

class Persona:
	def __init__(self, nombre, apellido):
		self.nombre=nombre
		self.apellido=apellido
		
	def get_nombre(self):
		return self.nombre
		
	def get_apellido(self):
		return self.apellido
		
	def set_nombre(self, nuevo_nombre):
		self.nombre = nuevo_nombre

	def set_apellido(self, nuevo_apellido):
		self.apellido = nuevo_apellido
		







