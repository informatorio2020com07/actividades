# -*- coding: utf-8 -*-
from funciones import *
#En otro archivo, importar las funciones creadas.


def comprobacion(texto):
	#comprueba que se ingrese un entero
	cifra=None
	while cifra==None:
		try:
			cifra=int(input (texto))
		except:
			print("no es una cifra valida")
	return cifra

def main():
	#Primero pregunte por una cantidad de segundos, y diga cuantas horas, minutos y segundos son.
	segundos=comprobacion("1 - ingresa una cantidad de segundos: ")
	horario=conversor_horario(segundos)
	print("el tiempo ingresado en segundos equivale a: \n horas: {0}, minutos: {1}, segundos: {2}".format(*horario))
	
	#Luego, preguntar por una cantidad de minutos y decir a cuantas horas, minutos y segundos representa.
	minutos=comprobacion("1 - ingresa una cantidad de minutos: ")
	segundos=conversor_segundos(minutos=minutos)
	horario2=conversor_horario(segundos)
	print("el tiempo ingresado en minutos equivale a: \n horas: {0}, minutos: {1}, segundos: {2}".format(*horario2))
	
	#Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter como "hs:mm:ss"
	tiempo="hs:mm:ss"
	#comprobando el formato
	while len(tiempo) != 3:
		print("ingresar una cantidad de tiempo expresada como: ")
		tiempo=input("hs:mm:ss ")
		tiempo=tiempo.split(":")
	#asegurandose que sean enteros
	for i in range (0,len(tiempo)):
		try:
			tiempo[i]=int(tiempo[i])
		except:
			tiempo[i]=0
	#Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos en distintas lineas.
	print("el tiempo ingresado es: \n -horas: {0} \n -minutos: {1} \n -segundos: {2}".format(*tiempo))
	tiempo_segundos=conversor_segundos(*tiempo)
	print("Equivale a: {0} Segundos.".format(tiempo_segundos))
	



if __name__ == "__main__":
    main()