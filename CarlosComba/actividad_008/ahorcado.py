import os
import random
# mostramos la pantalla esta en otro archivo
from mostrar_palabra import mostrar_palabra
# dibujar el muñeco esta en otro archivo
from muneco import dibujar
#variables usadas
#eleccion, palabra, lista, recibo, ciclo, juego1, control, 
#respuesta,num_intentos, falla, acierto, cant, intento,incognita, diccionario

# menu de inicio	
def menu():
	print("Bienvenido a Ahorcado Ahorcate un juego de 6 niveles")
	print("1 Desea Jugar")
	print("2 Desea Salir")
	eleccion=int(input("empecemos: "))
	return eleccion==1

# elige la palabra de manera random no repetida
def seleccionar_palabras_azar(ciclo,lista):
	palabra=random.choice(lista[0:len(lista)-ciclo])
	lista.remove(palabra)
	lista.append(palabra)
	return palabra

#solicitar letra
def solicitar_letra():
	recibo="None"
	while len(recibo)>1:
		recibo=input("Ingrese una Letra: ").lower()
	return recibo	

# funcion juego
def jugar(ciclo,respuesta):
	#//Carga inicial de palabra
	#guarda la palabra para jugar
	juego1=seleccionar_palabras_azar(ciclo,incognita)
	#guarda la respuesta correcta
	respuesta.clear()
	control=juego1[1:len(juego1)-1]
	for x in juego1[1:len(juego1)-1]:
		respuesta.append(" __ ")
	#limpia el menu
	os.system("cls")
	#imprime el encabezado y la palabra muestra
	print("")
	print("")
	print("\n Palabra ",ciclo+1)
	print("Pista: ",Diccionario[juego1])
	print("")
	mostrar_palabra(juego1,"",respuesta)
	falla=0
	#// fin de carga
	#//cuerpo principal
	while falla<7 and control!="".join(respuesta):
		intento=solicitar_letra()
		os.system("cls")
		print("")
		print("")
		print("\n Palabra ",ciclo+1)
		print("Pista: ",Diccionario[juego1])
		print("")
		print("")
		if intento in control:	
			print("Bravo")
		else:
			falla+=1
			print("Huuu")
		print("")	
		respuesta=mostrar_palabra(juego1,intento,respuesta)
		print("")
		print("")
		dibujar(falla)
	if falla<7:
		resultado=True
	else:
		resultado=False
	return	resultado

def despedida(ganadas):
	print("\n Gracias por jugar")
	print("\n Ganaste ",ganadas," partida")

def mensaje_ganar():
	print("\n GANASTE")
	
def mensaje_perder():
	print("\n PERDISTE")
	


#Main
respuesta=[]
incognita=["Armadillo","Albañil","Berruga","Maletin","Mercado","Travesura"]
muñeco=["O","|","/","] ","Ø",""]
Diccionario={"Armadillo":"Es un animal muy armado",
"Albañil":"Si no tenes uno, dificil que puedas armar tu casa",
"Berruga":"Siempre las viste acompañando una bruja",
"Maletin":"Si tenes uno sin plata, no sirve",
"Mercado": "Odiado por muchos, amados por algunos",
"Travesura":"lo hacias de chiquito"}
indice=0
victoria=0
while menu() and indice<6:
	if jugar(indice,respuesta):
		mensaje_ganar()
		victoria+=1
	else:
		mensaje_perder()
	indice+=1	
	print("")
	print("")
despedida(victoria)	
	