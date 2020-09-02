""" Realizar un función que reciba como parámetro una cantidad de
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

        Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter como "hs:mm:ss".
            Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos en distintas lineas.
            Luego mostrar a cuanto tiempo expresado en segundos equivale.
                
                Horas: 10
                Minutos: 30
                Segundos: 25
                Equivale a: 37825 Segundos.
"""
from datetime import * #datetime, timedelta
import time

def cantSegundos(numSegundos):

    hora = time.strftime("%H:%M:%S", time.gmtime(numSegundos))

    tupla = tuple(hora.split(":"))
    #tupla = time.mktime(hora.timetuple())

    """
    hora = tuple(timedelta(seconds=numSegundos))             #timedelta(seconds=numSegundos)
        
    h = hora.hour()
    m = hora.minute()
    s = hora.second()
    """
    return tupla     #(h, m, s)

#print(cantSegundos(37000))         # --> ('10', '16', '40')

def devuelveSegundos(hora=0, minuto=0, segundo=0):

    totalSegundos = (hora*3600) + (minuto*60) + segundo

    return totalSegundos

#print(devuelveSegundos(10, 16, 40)) # --> 37000
#print(devuelveSegundos(segundo=10, hora=1))     # --> 3610

if __name__ == "__main__":

    print("hola desde actividad2")