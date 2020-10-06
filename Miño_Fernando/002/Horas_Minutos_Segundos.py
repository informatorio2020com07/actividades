"""

002-
    Realizar un función que reciba como parámetro una cantidad de
    segundos, y devuelva una tupla con la cantidad de segundos
    expresada en hh,mm,ss.

    Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos. Y que retorne la suma de estos expresanda en segundos. (Los parámetros, son opcionales y por defecto sus valores 0.)
------------------------------------------
    En otro archivo, importar las funciones creadas.
    Realizar un programa que:
        
        Primero pregunte por una cantidad de segundos, y diga cuantas horas, minutos y segundos son.
        
        Luego, preguntar por una cantidad de minutos y decir a cuantas
        horas, minutos y segundos representa.

        Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter como "hs:mm:ss".
            Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos en distintas lineas.
            Luego mostrar a cuanto tiempo expresado en segundos equivale.
                
                Horas: 10
                Minutos: 30
                Segundos: 25
                Equivale a: 37825 Segundos.



def Transf_Seg(seg):
	hh = seg//3600
	mm = seg%3600//60
	ss = seg%3600%60
	return hh,mm,ss

def Sumador(hh=0,mm=0,ss=0):
	sumador = hh*3600+mm*60+ss
	return sumador

"""
import time
import os
from Hora_Min_Seg import *



def Menu():
	print (" \n                              Menu:\n\n                             0 - Salir\n")
	print (" \n                             1 - Segundos:\n\n [ Ingresar segundos y devolvemos Su equivalencia en: Hora-Minutos-Segudno ]")
	print (" \n\n                            2 - Minutos:\n\n [ Ingresar Minutos y devolvemos Su equivalencia en: Hora-Minutos-Segudno ]\n\n\n                            3- Sumador:\n\n [ Se suman los valores que se ingresan y devolvemos su equivalencia en: Hora-Minutos-Segudno ]\n\n")

    
    

def Sumar():

    while True:
        try:

            hora = int(input("\ningrese cantidad de horas: "))
            break

        except ValueError:
            print ("\n\nError, no debe ingresar un caracter ni comas o puntos: \n\n")
            os.system("pause")
            os.system("cls")

    os.system("cls")
    while True:
        try:

            minuto = int(input("\n\ningrese cantidad de minutos: "))
            break

        except ValueError:
            print ("\n\nError, no debe ingresar un caracter ni comas o puntos: \n\n")
            os.system("pause")
            os.system("cls")


    os.system("cls")
    while True:
        try:

            segundo = int(input("\n\ningrese cantidad de segundos: "))
            break

        except ValueError:
            print ("\n\nError, no debe ingresar un caracter ni comas o puntos: \n\n")
            os.system("pause")
            os.system("cls")

    os.system("cls")
    cantidad_Horas(hora, minuto, segundo)




print ("\n\n\n\n\n\n\n\n\n                          Bienvenido\n\n\n")


while True:

    try:


        Menu()
        menu = int(input ("ingrese un valor del 0 al 3: "))

        if menu in range(4):

            if (menu == 0):
            
                break
            
            elif (menu == 1):

                os.system("cls")

                while True: 
                	try: 
                		segundos = int (input ("\n\ningrese la cantidad de Segundos: "))
                		break
                	except:
                		print ("\n\nDebe ingresar un Numero sin comas ni puntos\n\n")
                		os.system("pause")
                		os.system("cls")



                print ("A continuacion, mostramos esos segundos en horas-minutos-segundos\n\n")
                Transf_Seg(segundos)
                os.system("pause")
                os.system("cls")
            
            elif (menu == 2):
                
                os.system("cls")
                while True: 
                	try: 
                		minutos = int (input ("Ingrese Minutos: "))
                		break
                	except:
                		print ("\n\nDebe ingresar un Numero sin comas ni puntos\n\n")
                		os.system("pause")
                		os.system("cls")

                
                Transf_Min(minutos)
                os.system("pause")
                os.system("cls")
            
            elif (menu == 3):
                os.system("cls")
                Sumar()
                os.system("pause")
                os.system("cls")
            
        else:
            print ("\nDebe ingresar [0]-[1]-[2]-[3]\n")


        os.system("pause")
        os.system("cls")
    
    except ValueError:
    
        print ("\nError, Debe ingresar un Entero sin comas ni puntos \n")
        os.system("pause")
        os.system("cls")





