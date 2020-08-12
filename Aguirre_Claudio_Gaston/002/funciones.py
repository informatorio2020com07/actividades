# -*- coding: utf-8 -*-
#Realizar un función que reciba como parámetro una cantidad de segundos, y devuelva una tupla con la cantidad de segundos expresada en hh,mm,ss.

def conversor_horario(segundos):
	horas=segundos//3600
	minutos=(segundos%3600)//60
	segundos=(segundos%3600)%60
	return (horas, minutos, segundos)
	
#Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos. Y que retorne la suma de estos expresanda en segundos. (Los parámetros, son opcionales y por defecto sus valores 0.)
	
def conversor_segundos(horas=0, minutos=0, segundos=0):
	segundos=(horas*3600)+(minutos*60)+segundos
	return segundos


