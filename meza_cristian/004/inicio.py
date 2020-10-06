'''
Un programa que permita escribir varios modelos de cartas/notas
y que después pueda seleccionar un modelo de nota, y que me generé
varias notas reemplazando los destinatarios con una lista de nombres
que se le pase y el nombre del remitente indicado.
'''
from modelo import *
from time import sleep

limpiar_pantalla()
menu = True
while menu:
    try:
        print("Favor Seleccionar Opcion:")
        res = int(input("1- Cargar Modelo de Nota/Carta\n2- Listar Nota/Carta\n3- Enviar Nota/Carta\n0- Salir\nOpcion: "))
        if res == 1:
            limpiar_pantalla()
            cargar_modelo()
            limpiar_pantalla()
        elif res == 2:
            limpiar_pantalla()
            print("Listado de Modelos:\n")
            seleccionar_modelo(2)
            input()
            limpiar_pantalla()
        elif res == 3:
            limpiar_pantalla()
            seleccionar_modelo(3)
            limpiar_pantalla()
            cargar_destinatario()
            limpiar_pantalla()
            remit=input("Ingrese nombre del Remitente: ")
            limpiar_pantalla()
            mostrar(remit)
            sleep(5)
            limpiar_pantalla()
        elif res == 0:
            menu = False
        else:
            print("Volver a Intentar!")
            sleep(1)
            limpiar_pantalla()
    except:
        #print("Error en Seleccion. Volver a Intentar!")
        sleep(1)
        limpiar_pantalla()

limpiar_pantalla()
print("Muchas Gracias. Vuelva Pronto!")



