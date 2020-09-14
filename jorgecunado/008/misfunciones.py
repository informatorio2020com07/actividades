import os

def imprimo_ahorcado(perrados):
	'''recibo la cantidad de errados y dibujo el muñequito de a cuerdo a la '''
	'''cantidad de los errados'''

	if perrados == 0:
		print("------")
		print("!     ")
		print("!     ")
		print("!     ")
		print("!     ")
		print("!     ")
	elif perrados == 1:
		print("------")
		print("!     O")
		print("!     ")
		print("!     ")
		print("!     ")
		print("!     ")
	elif perrados == 2:
		print("------")
		print("!     O")
		print("!     │")
		print("!     ")
		print("!     ")
		print("!     ")
	elif perrados == 3:
		print("------")
		print("!     O")
		print("!     │")
		print("!     │")
		print("!     ")
		print("!     ")
	elif perrados == 4:
		print("------")
		print("!     O")
		print("!    <│>")
		print("!     │")
		print("!     ")
		print("!     ")
	elif perrados == 5:
		print("------")
		print("!     O")
		print("!    <│>")
		print("!     │")
		print("!    ┌ ┐")
		print("!     ")
	elif perrados == 6:
		print("------")
		print("!     O")
		print("!   -----")
		print("!    <│>")
		print("!     │")
		print("!    / '\'")
		print("!     ")
		z=input("A H O R C A D O")


def chequear_ingresada(lingresada,listaingr):
	'''Recibo la letra ingresada y la lista de letras ingresadas anteriormenete y me fijo si la'''
	'''letra esta dntro de lista dev falo o no esta dev true, aparte veo q sea alfabetico.'''
	
	ulingresada=lingresada.upper()
	
	if ulingresada.isalpha():
		
		if ulingresada in listaingr:
			print("Ya ingreao la {}".format(lingresada))
			z=input(" ")
			return False
		else:
			listaingr.append(ulingresada)
			return True
	
	else:		
		print("Debe ingresar una letra, no se permite otro caracter")
		z=input(" ")
		return False

def lista_a_cadena(listacad):
	'''recibe una LISTA y la pasa a una VARIABLE cadena '''
	
	cadena = ""
	for i in listacad:
		if i != "":
			cadena += i
	return cadena

def proc_nogano(ppalabra,pnueva_palabra,plistaing, perrados):
	'''Recibe la palabra a adivinar, la lista nueva_palabra, y los errados,'''
	''' Avisa que perdio al ahorcado-Dentro de esta funcion llamo a otra def x mi.'''
	
	imprimo_ahorcado(perrados)
	print(" ")
	print("Palabra a adivinar : {}".format(ppalabra))
	print("")	
	print(pnueva_palabra)
	print(" ") 		 	
	print("UD. ESTA MUERTO. HA SIDO AHORCADO. No tiene mas oportunidades")
	print(" ")
	print("Letras ingresadas : ", plistaing)

def proc_gano(pnueva_palabra):
	'''Recibe la lista nueva palabra, la imprime y avisa q gano.'''
	#os.system("cls")
	print(" ")
	print(" ")
	print(pnueva_palabra)
	print("*************** G A N A S T E *******************")
	z = input("Presione cualquier tecla para seguir...")
	return 10, True

