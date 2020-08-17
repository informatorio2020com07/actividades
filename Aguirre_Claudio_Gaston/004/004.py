#-*- coding: utf-8 -*- 
#Un programa que permita escribir varios modelos de cartas/notas y que después pueda seleccionar un modelo de nota, y que me genere varias notas reemplazando los destinatarios con una lista de nombres que se le pase y el nombre del remitente indicado.
import os
import sys

def carta():
#permite escribir cartas/notas 
	print('Para finalizar ingresa un espacio en blanco " " en un renglón nuevo')
	print("Puedes escribir tu carta: ")
	carta=[]
	renglon = input("")
	while renglon != " ":
		carta.append(renglon)
		renglon = input("")
	return carta

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
	

	
def main():
	
	
	opciones=("""
Elige modelo de carta
    1:
    ----
        Estimado (nombre):
            Le damos la bienvenida al servicio.

        Con afecto,
            (nombre_remitente)
    ----
    2:
    ----
        Señor/a (nombre):
            De mi mayor consideracion.

        Atte,
            (nombre_remitente)
    ----
    3:
    ----
        Señor/a (nombre):
            Le damos la bienvenida al servicio.

        Atte,
            (nombre_remitente)
    ----
""")
	modelos = {    "1" : """
    ----
        Estimado {0}:
            Le damos la bienvenida al servicio.
  {2}

        Con afecto,
            {1}
    ----""",
    "2" : """
    ----
        Señor/a {0}:
            De mi mayor consideración.
  {2}

        Atte,
            {1}
    ----""",
    "3" : """
    ----
        Señor/a {0}:
            Le damos la bienvenida al servicio.
  {2}
			
        Atte,
            {1}
    ----""",
	}
	#seleccion de un modelo de nota
	bucle=True
	while bucle:
		os.system("Cls") 
		print(opciones)
		eleccion = input("Elige una opción válida: ")
		modelo = modelos.get(eleccion)
		if modelo:
			bucle=False
		else:
			print("{0} no es una elección válida".format(eleccion))
	rtte=input("ingrese nombre del Remitente: ")
	nombres=names()
	escrito=carta()
	#genera varias cartas reemplazando los destinatarios con una la lista de nombres y el nombre del remitente indicado
	for nombre in nombres:
		cartas = ""
		cartas = (modelo.format(nombre,rtte,'\n'.join("{}".format(renglon)
		for renglon in escrito)))
		print (cartas)
	
main()	

		
		
