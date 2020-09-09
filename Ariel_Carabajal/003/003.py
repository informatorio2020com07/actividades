#!/usr/bin/python3
'''
003- 
    Crear una clase Persona, que tenga atributo nombre y apellido, 
    y los metodos get y set para cada atributo.
'''

class Persona:

	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def get_nombre(self):
		return self.nombre

	def get_apellido(self):
		return self.apellido

	def set_nombre(self, nuevoNombre):
		self.nombre = nuevoNombre

	def set_apellido(self, nuevoApellido):
		self.apellido = nuevoApellido


waino = Persona("Jaimito", "Fulanito")

print(waino.get_nombre(), waino.get_apellido())

waino.set_nombre("Juanita")

waino.set_apellido("Morosa")

print(waino.get_nombre(), waino.get_apellido())