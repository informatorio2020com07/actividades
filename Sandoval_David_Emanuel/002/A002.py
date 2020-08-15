# 002-
#     Realizar un función que reciba como parámetro una cantidad de
#     segundos, y devuelva una tupla con la cantidad de segundos
#     expresada en hh,mm,ss.

#     Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos. 
#     Y que retorne la suma de estos expresanda en segundos. (Los parámetros, son opcionales y por defecto sus valores 0.)

#     En otro archivo, importar las funciones creadas.
#     Realizar un programa que:
        
#         Primero pregunte por una cantidad de segundos, y diga cuantas horas, minutos y segundos son.
        
#         Luego, preguntar por una cantidad de minutos y decir a cuantas
#         horas, minutos y segundos representa.

#         Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter como "hs:mm:ss".
#             Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos en distintas lineas.
#             Luego mostrar a cuanto tiempo expresado en segundos equivale.
                
#                 Horas: 10
#                 Minutos: 30
#                 Segundos: 25
#                 Equivale a: 37825 Segundos.


def seconds_to_hhmmss(segundos: int):
    """Convierte la cantidad de segundos pasados como argumento a una tupla de (hh, mm, ss)"""
    minutos = segundos//60
    horas = minutos//60
    return horas, minutos - horas * 60, segundos - minutos * 60


def hhmmss_to_seconds(hours=0, minutes=0, seconds=0):
    """Pasa las horas, minutos y segundos a su total en segundos"""
    seconds_in_hours = hours * 60 * 60
    seconds_in_mins = minutes * 60
    return seconds + seconds_in_mins + seconds_in_hours


if __name__ == "__main__":
    segundos = 3453543534351
    print(seconds_to_hhmmss(segundos))
    print(segundos == hhmmss_to_seconds(*seconds_to_hhmmss(segundos))) # should be true
