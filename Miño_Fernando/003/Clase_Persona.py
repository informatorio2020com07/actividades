"""

003- 
    Crear una clase Persona, que tenga atributo nombre y apellido, y los metodos get y set para cada atributo.

"""

class Persona():

	def __init__(self, nombre="Ningun nombre", apellido = "Ningun apellido"):
		self.__nombre=nombre
		self.__apellido=apellido

	def get_Mostrar_Nombre(self):#Emitir atributo nombre
		return self.__nombre
	
	"""
	def dniEmitir(self):
		return self.dni
	"""
	
	def get_Mostrar_Apellido(self):#Emitir atributo apellido
			return self.__apellido

	def set_Actualizar_Nombre(self,nombrenuevo):
		self.__nombre = nombrenuevo


	def set_Actualizar_Apellido(self, apellidonuevo):
		self.__apellido = apellidonuevo


"""
Julian = Persona()

print (Julian)# No emite que es una clase
#print (Julian.dniEmitir())
print (Julian.get_Mostrar_Nombre())# No emite el contenido dentro del atributo nombre el cual es encapsulado
print (Julian.get_Mostrar_Apellido())# No emite el contenido dentro del atributo apellido el cual es encapsulado

nombrenuevo = input("ingrese un nuevo nombre: ") 
apellidonuevo = input ("ingrese un nuevo apellido: ")
Julian.set_Actualizar_Nombre(nombrenuevo)
print (Julian.get_Mostrar_Nombre())# No emite el contenido dentro del atributo nombre el cual es encapsulado

Julian.set_Actualizar_Apellido(apellidonuevo)
print (Julian.get_Mostrar_Apellido())# No emite el contenido dentro del atributo apellido el cual es encapsulado


"""