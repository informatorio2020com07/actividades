#003- 
#Crear una clase Persona, que tenga atributo nombre y apellido, y los metodos get y set para cada atributo.
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre):
        return self.nombre

    def get_apellido(self):
        return self.apellido
    
    def set_apellido(self,apellido):
        return self.apellido
    


