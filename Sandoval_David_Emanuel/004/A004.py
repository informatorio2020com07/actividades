class NoteManager:
    """Se encarga de gestionar los distintos modelos de notas, en forma de strings."""
    def __init__(self, *args, **kwargs):
        self.modelos = {}
        self.cargar_modelos_por_defecto()

    def create_modelo(self):
        nombre = input("Escriba el nombre del modelo: ")
        print(""""\nEscriba el cuerpo de la nota. Puede escribir <remitente> y <destinatario> en lugar de los nombres reales.
                Escriba 'END' para terminar y presione enter.""")
        print(f"""Ej: \n{self.get_modelo("estandar")}""")
        cuerpo = ""
        insertando = True
        while insertando:
            linea = input(">> ")
            if linea.endswith("END"):
                insertando = False
                linea = linea.strip("END")
            cuerpo += linea + "\n"

        self.add_modelo(nombre, cuerpo)
        print("Modelo agregado")
        print("Nombre:", nombre)
        print("Cuerpo:", self.modelos.get(nombre))
        print(self.modelos.get("estandar"))

    def add_modelo(self, nombre, cuerpo):
        self.modelos[nombre] = cuerpo

    def borrar_modelo(self):
        self.listar_modelos()
        while True:
            modelo_a_borrar = input("ingrese el modelo a borrar: ")
            if modelo_a_borrar:
                try:
                    del self.modelos[modelo_a_borrar]
                    print("Modelo borrado con éxito")
                    break
                except KeyError:
                    print(
                        "Ese modelo de nota no existe, intente nuevamente, o pulse enter para cancelar")
            else:
                break

    def listar_modelos(self):
        for num, modelo in enumerate(self.modelos):
            print(num + 1, ")", modelo)

    def get_modelos(self):
        return self.modelos

    def cargar_modelos_por_defecto(self):
        estandar = """
            Estimado <destinatario>:
                Le damos la bienvenida al servicio.

            Con afecto,
                <remitente> """

        comercial = """
            Estimado Sr. cliente <destinatario>:
                Le damos la bienvenida al servicio.
                Esperamos que sea de su agrado.

                Ante cualquier consulta estamos en contacto con usted.

            Con afecto,
                <remitente> """

        casual = """
            Hola <destinatario>:

            Te saluda tu amiogo <remitente>. :) """
        self.modelos["estandar"] = estandar
        self.modelos["comercial"] = comercial
        self.modelos["casual"] = casual

    def get_modelo(self, nombre_modelo):
        return self.modelos.get(nombre_modelo)

    def get_nombre_por_indice(self, indice):
        """Devuelve el nombre de un modelo de nota según el índice que le pasemos"""
        if indice <= len(self.modelos):
            for i, nombre_modelo in enumerate(self.modelos.keys()):
                if i == indice - 1:
                    return nombre_modelo


class Note:
    """Construye y define una nota con los parámetros pasados"""
    def __init__(self, remitente=None, destinatario=None,
                 body=None, tipo=None, **kwargs):
        self.remitente = remitente
        self.destinatario = destinatario
        self.body = body
        self.tipo = tipo

    @classmethod
    def from_args(cls, *args, **kwargs):
        """Crea una nueva instacia de Note con los argumentos pasados"""
        return cls(*args, **kwargs)

    def set_remitente(self, nombre_remitente):
        self.remitente = nombre_remitente

    def get_remitente(self):
        return self.remitente

    def set_destinatario(self, nombre_detinatario):
        self.destinatario = nombre_detinatario

    def get_destinatario(self):
        return self.destinatario

    def build_body(self):
        self.body = self.body.replace("<destinatario>", self.destinatario)
        self.body = self.body.replace("<remitente>", self.remitente)

    def get_body(self):
        self.build_body()
        return self.body


class NoteSender:
    """Se encarga de pedir información al usuario para enviar las notas."""
    def __init__(self, note_model: Note, note_manager: NoteManager, **kwargs):
        self.note_manager = note_manager
        self.note_model = note_model
        self.remitente = None
        self.destinatarios = None
        self.notas = []

    def listar_modelos_nota(self):
        self.note_manager.listar_modelos()

    def pedir_seleccion_modelo(self):
        """Pide al usuario que elija un modelo de nota"""
        seleccion = None
        while True:
            print("Modelos de Nota\n")
            self.listar_modelos_nota()
            print("0 ) Salir")
            seleccion = input("Selecciona un modelo: ")
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if seleccion in range(len(self.note_manager.get_modelos()) + 1):
                    if seleccion == 0:
                        return seleccion
                    print("Modelo elegido:", self.note_manager.get_nombre_por_indice(seleccion))
                    break
                else:
                    print("Indique un número válido")
            else:
                print("Debe indicar un número")
        return seleccion

    def pedir_remitente(self):
        print()
        self.remitente = input("Remitente: ")

    def pedir_destinatarios(self):
        """Pide al usuario una lista de destinatarios"""
        if self.destinatarios is None:
            self.destinatarios = []
        print("Ingrese la lista de destinatarios, para terminar presione <enter>\n")
        while True:
            destinatario = input("Destinatario: ")
            if destinatario:
                self.destinatarios.append(destinatario)
            else:
                break

    def enviar_notas(self):
        """Construye las notas y las 'envía'"""
        # pedimos que seleccione un modelo, devuelve un número
        modelo_nota = self.pedir_seleccion_modelo()
        if modelo_nota == 0:
            # Si es cero, salimos
            return
        # pedimos el nombre del modelo dado, según el número elegido 
        # en el menu de seleccion de modelos
        nombre_modelo_nota = self.note_manager.get_nombre_por_indice(modelo_nota)
        self.pedir_remitente()
        self.pedir_destinatarios()
        if nombre_modelo_nota:
            cuerpo_modelo_nota = self.note_manager.get_modelo(nombre_modelo_nota.lower())
            for destinarario in self.destinatarios:
                note = self.note_model.from_args(remitente=self.remitente, destinatario=destinarario,
                                                 body=cuerpo_modelo_nota, tipo=nombre_modelo_nota)
                note.build_body()
                self.notas.append(note)
        # Enviamos las notas que tengamos
        for nota in self.notas:
            print("  ENVIADO  ".center(80, "#"))
            print(nota.get_body())
            

def main():
    # Función principal, instancia las clases necesarias, NoteManager y NoteSender
    note_manager = NoteManager()
    note_sender = NoteSender(note_model=Note, note_manager=note_manager)
    note_sender.enviar_notas()


if __name__ == "__main__":
    main()
