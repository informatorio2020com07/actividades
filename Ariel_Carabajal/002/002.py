#!/usr/bin/python3
'''
002-
    Realizar un función que reciba como parámetro una cantidad de
    segundos, y devuelva una tupla con la cantidad de segundos
    expresada en hh,mm,ss.
    Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos. 
    Y que retorne la suma de estos expresanda en segundos. 
    (Los parámetros, son opcionales y por defecto sus valores 0.)
    En otro archivo, importar las funciones creadas.
    Realizar un programa que:
        
        Primero pregunte por una cantidad de segundos, y diga cuantas horas, minutos y segundos son.
        
        Luego, preguntar por una cantidad de minutos y decir a cuantas
        horas, minutos y segundos representa.
        Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter 
        como "hs:mm:ss".
            Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos en distintas lineas.
            Luego mostrar a cuanto tiempo expresado en segundos equivale.
                
                Horas: 10
                Minutos: 30
                Segundos: 25
                Equivale a: 37825 Segundos.
'''

def convHorario(segundos):
	horas = segundos // 3600
	minutos = (segundos % 3600) // 60
	segundos = (segundos % 3600) % 60
	return (horas, minutos, segundos)
	

def convSegundos(horas=0, minutos=0, segundos=0):
	segundos=(horas * 3600) + (minutos * 60) + segundos
	return segundos