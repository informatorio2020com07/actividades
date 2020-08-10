'''
Realizar un función que reciba como parámetro una cantidad de segundos, y devuelva una tupla con la cantidad de segundos
expresada en hh,mm,ss.
Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos.
Y que retorne la suma de estos expresanda en segundos. (Los parámetros, son opcionales y por defecto sus valores 0.)

En otro archivo, importar las funciones creadas.
Realizar un programa que:
    Primero pregunte por una cantidad de segundos, y diga cuantas horas, minutos y segundos son.
    Luego, preguntar por una cantidad de minutos y decir a cuantas horas, minutos y segundos representa.
    Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter como "hs:mm:ss".
    Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos en distintas lineas.
    Luego mostrar a cuanto tiempo expresado en segundos equivale.
      Horas: 10
      Minutos: 30
      Segundos: 25
      Equivale a: 37825 Segundos.
'''
from conversor import *
seg=int(input("Ingresar Cantidad de Segundos: "))
print("Segundos Expresados en HH:MM:SS = ",segundos_HMS(seg))
min=int(input("Ingresar Cantidad de Minutos: "))
print("Minutos Expresados en HH:MM:SS = ",segundos_HMS(min*60))
cadena=input("Ingresar Horas Minutos y Segundos con el siguiente formato = hs:mm:ss : ")
cadena=cadena.split(":")
print("Horas: ",cadena[0])
print("Minutos: ",cadena[1])
print("Segundos: ",cadena[2])
convert=total_segundos(int(cadena[0]),int(cadena[1]),int(cadena[2]))
print("Equivale a: {seg} Segundos.".format(seg=convert))
print("Segundos Expresados en HH:MM:SS = ",segundos_HMS(convert))



