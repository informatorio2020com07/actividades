#Crear una clase Persona, que tenga atributo nombre y apellido, 
#y los metodos get y set para cada atributo.

class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
