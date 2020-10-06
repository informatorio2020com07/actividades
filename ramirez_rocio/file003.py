"""003- 
    Crear una clase Persona, que tenga atributo nombre y apellido, y los metodos
    get y set para cada atributo."""

class Persona:
	def __init__(self,nombre, apellido):
		self.nombre=nombre
		self.apellido=apellido

	def get_persona(self):
		print("Nombre: ", self.nombre)
		print("Apellido: ", self.apellido)

	def set_nombre(self, new_nombre):  # el metodo set sirve para poder modificar los valores del atributo
		self.nombre=new_nombre

	def set_apellido(self, new_apellido):
		self.apellido=new_apellido


persona1=Persona("rocio", "ramirez")

print("Crendo el primer objeto de clase Persona:'persona1' ")
persona1.get_persona()

print(" ")

print("Modificando el apellido del objeto:'persona1' ")	

persona1.set_apellido("Merker")
persona1.get_persona()