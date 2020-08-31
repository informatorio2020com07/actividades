#Crear una clase Persona, que tenga atributo nombre y apellido, 
#y los metodos get y set para cada atributo.
class Persona:
	def __init__(self,nombre,apellido):
		self.__nombre=nombre
		self.__apellido=apellido

	def get_nombre(self):
		return self.__nombre

	def get_apellido(self):
		return self.__apellido

	def set_nombre(self):
		self.__nombre=nombre

	def set_apellido(self):
		self.__apellido=apellido

persona1=Persona("Rosana","Palavecino")

print(persona1.get_nombre())
print(persona1.get_apellido())
