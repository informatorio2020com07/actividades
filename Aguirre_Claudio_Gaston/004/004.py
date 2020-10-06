import os
import sys
from io import open

#Un programa que permita escribir varios modelos de cartas/notas y que después pueda seleccionar un modelo de nota, y que me genere varias notas reemplazando los destinatarios con una lista de nombres que se le pase y el nombre del remitente indicado.

def nuevo_model(opcion):
#permite escribir cartas/notas 
	print('Para finalizar ingresa un espacio en blanco " " en un renglón nuevo')
	print("Puedes escribir tu carta: ")
	car="carta{}.txt".format(opcion)
	carta=open(car,"w")
	renglon = input("")
	while renglon != " ":
		renglon = renglon+"\n"
		carta.write(renglon)
		renglon = input("")
	carta.close()
	return 

def mostrar_guardados(frase):
#muestra modelos guardados
	os.system("Cls") 
	
	for i in range (1,4):
		print(" {} : _".format(i))
		imprimir_carta("(nombre)","(rtte)",i)
	print(frase)
	opcion = input("opción: ")
	return opcion

def imprimir_carta(nombre,rtte,eleccion):
	base="""
    ----
        Señor/a {0}:
  {2}

        Atte,
            {1}
    ----"""
	car="carta{}.txt".format(eleccion)
	carta=open(car,"r")
	modelo=carta.read()
	print(base.format(nombre, rtte, modelo))
	print(" ")
	carta.close
	return
	
def names():
#crea lista de nombres mediante inputs
	lista_nombres = []
	cont=1
	print("Ingresa nombre del/los receptores de la/s cartas")
	print('Ingresa un espacio en blanco " " para finalizar')
	nombre = input("Destinatario {}: ".format(cont))
	while nombre != " ":
		cont += 1
		lista_nombres.append(nombre)
		nombre = input("Destinatario {}: ".format(cont))
	return lista_nombres		
	
def salir():
    
    sys.exit(0)
	
def main():	
	while True:
		os.system("Cls") 	
	
		print("1 - Nuevo modelo de carta")
		print("2 - Elige un modelo existente")
		print("3 - salir")
		opcion_menu=input("elige una opcion: ")
		lista_opcion=("1","2","3") #para seleccion de un modelo de nota
		
		if opcion_menu == "1":		
			opcion=mostrar_guardados("elige modelo que quieres sobreescribir: ")
			while opcion not in lista_opcion:
				opcion=mostrar_guardados("elige modelo que quieres sobreescribir: ")
			nuevo_model(opcion)
		if opcion_menu == "2":
			opcion=mostrar_guardados("elige el modelo que quieres imprimir: ")
			while opcion not in lista_opcion:
				opcion=mostrar_guardados("elige el modelo que quieres imprimir: ")
			rtte=input("ingrese al emisor de la carta: ")
			lista_nombres=names()
			#genera varias cartas reemplazando los destinatarios con una la lista de nombres y el nombre del remitente indicado
			for nombre in lista_nombres:
				imprimir_carta(nombre,rtte,opcion)

			input("volver a menú")
		if opcion_menu == "3":
			salir()
main()