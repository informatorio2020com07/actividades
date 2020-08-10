 class Persona:
 	def __init__(self,nombre,apellido):
 		self.__nombre=nombre
 		self.__apellido=apellido

 	def get_nombre(self):
 		return self.__nombre

 	def set_nombre(self,nombre):
 		self.__nombre=nombre

 	def get_apellido(self,apellido):
 		return self.__apellido

 	def set_apellido(self,apellido):
 		self.__apellido