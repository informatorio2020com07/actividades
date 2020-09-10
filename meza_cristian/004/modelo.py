from os import system

mod = "Estimado (nombre): Le damos la bienvenida al servicio. Con afecto, (nombre_remitente)"

global list_mod
list_mod = [mod]
global list_nombre
list_nombre = []

def limpiar_pantalla():
    system("cls")


def cargar_modelo():
    sigue_cargando = True
    while sigue_cargando:
        modelo_ingresar = input(
            "Cargar la Nota/Carta siguiendo las siguientes instrucciones:\n(nombre) para destinatario\n(nombre_remitente) para remitente\nPara terminar carga Enter\n")
        if modelo_ingresar == "":
            sigue_cargando = False
        else:
            global list_mod
            list_mod.append(modelo_ingresar)
            limpiar_pantalla()


def cargar_destinatario():
    sigue_cargando = True
    while sigue_cargando:
        destinatario = input("ingrese nombre destinario: (deje vacio para cortar la carga)\n")
        if destinatario == "":
            sigue_cargando = False
        else:
            global list_nombre
            list_nombre.append(destinatario)
            limpiar_pantalla()


def seleccionar_modelo(op):
    global list_mod
    for indice, modelo in enumerate(list_mod):
        print(indice, end="-")
        print(modelo)
    if (op == 3):
        opcion = int(input("seleccione una Nota/Carta: "))
        global modelo_elegido
        modelo_elegido = list_mod[opcion]


def mostrar(remitente):
    global modelo_elegido
    global list_nombre
    __imprimir_completo(modelo_elegido, list_nombre, remitente)


def __imprimir_completo(mensaje, destinos, remitente):
    for destinario in destinos:
        carta_imprimir = modelo_elegido.replace("(nombre)", destinario)
        carta_imprimir = carta_imprimir.replace("(nombre_remitente)", remitente)
        print(carta_imprimir)
