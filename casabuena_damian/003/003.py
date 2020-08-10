class persona:
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre_nuevo):
        self.nombre=nombre_nuevo

    def get_apellido(self):
        return self.apellido

    def set_apellido(self,apellido_nuevo):
        self.apellido=apellido_nuevo

p1=persona("Alejandro", "Pérez")
print(p1.get_nombre())
print(p1.get_apellido())

p1.set_nombre("Diego")
p1.set_apellido("Morales")
print(p1.get_nombre())
print(p1.get_apellido())