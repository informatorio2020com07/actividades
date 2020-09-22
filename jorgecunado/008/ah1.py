import os
import random				# importo lo q voy a necesitar
from misfunciones import *

lpalabras = "texto mundo elipse maraton metamorfosis formosa vaso mendoza popular mision" 
lpalabras += " andaluz avion meza ambulancia mula bandalo"

palabras = lpalabras.split()        # paso la cadena lpaplabras a la lista de palabas. 
palabra = random.choice(palabras)	# elijo una aleatoriamente
palabra = palabra.upper()			# la paso a mayuscula
lista_palabra = list(palabra)       # paso la palabra elejida a una lista de letras
nueva_palabra = [""]*len(palabra)	# creo una lista pseudo vacia con nulos "" pp letras acertadas
listaing=[]							# creo otra lista para reistrar las letras ingesadas
errados = 0							# inicializo los intentos errados
gano = False						# inicializo la variable par saber si gano

os.system("cls")

while errados <= 5:
	
	letravalida=False				# digo q no es letra valida
	
	while not letravalida:			# hago mientras la condicion Verdad. 
		imprimo_ahorcado(errados)   # llamo a la funcion imrimo ahorcado y le paso los errados
		print(" ")
		print(nueva_palabra)		# imprimo la palabra que se va fomando
		print("")
		print("INTENTOS FALLIDOS: {}, TE QUEDAN {}".format(errados, 6 - errados))
		print(" ")
		letra=input("INGRESE UNA LETRA:")
		letra=letra.upper()
		letravalida=chequear_ingresada(letra,listaing) # chequeo q sea letra y no la hayamos ing.
													   # con la funcion chequar_ingresado
		os.system("cls")            # limpio la pantalla
		
	if letra in lista_palabra:		# pregunto si la letra ingresada esta contenida en la palabra
		for i in range(0,len(lista_palabra)): # recorro la lista exe para saber dde esta
			if lista_palabra[i] == letra: # cuando la encuentro
				nueva_palabra[i] = letra  # pongo en la lista que se va formando la letra en la 
										  # la posicion q debe ir
		penformacion = lista_a_cadena(nueva_palabra) # paso lo q ingrese a cadena 	
		if penformacion == palabra: # comparo si la palabra q voy ingresando = palabra
			errados, gano = proc_gano(nueva_palabra) # si la cond. ant es v llamo a proc_gano
			
	else:  # si la letra no esta en lista_palabra 
		errados += 1  # erre
	# de aca me voy a chquear el while de los errados para ver si sigo o trmino	
if not gano:
	proc_nogano(palabra, nueva_palabra, listaing, errados)
	
