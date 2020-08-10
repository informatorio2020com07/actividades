import math

def transformar_segundos(segundos):
    """transforma las horas,minutos y segundos en segundos"""
    horas=math.trunc(segundos//3600)
    minutos=math.trunc(segundos%3600//60)
    segundo=math.trunc(segundos%3600%60)
    return (horas,minutos,segundo)

def sumar_segundos(hora=0,minuto=0,segundo=0):
    """realiza la suma de hora,minutos y segundo a segundos"""
    segsuma=hora*3600+minuto*60+segundo
    return segsuma 

def transformar_minutos(minutos):
    """transforma los minutos con coma en segundos usando la funcion"""
    return transformar_segundos(minutos*60)


