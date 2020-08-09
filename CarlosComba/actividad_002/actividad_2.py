"""Realizar un función que reciba como parámetro una cantidad de
    segundos, y devuelva una tupla con la cantidad de segundos
    expresada en hh,mm,ss.

    Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos. Y que retorne la suma de estos 
    expresanda en segundos. (Los parámetros, son opcionales y por defecto sus valores 0.)

    En otro archivo, importar las funciones creadas.
    Realizar un programa que:
        
        Primero pregunte por una cantidad de segundos, y diga cuantas horas, minutos y segundos son.
        
        Luego, preguntar por una cantidad de minutos y decir a cuantas
        horas, minutos y segundos representa.

        Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter como "hs:mm:ss".
            Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos 
            en distintas lineas.
            Luego mostrar a cuanto tiempo expresado en segundos equivale.
                
                Horas: 10
                Minutos: 30
                Segundos: 25
                Equivale a: 37825 Segundos."""
import math
def transformar_segundos(segundos):
    """transforma las horas,minutos y segundos en segundos"""
    horas=math.trunc(segundos//3600)
    minutos=math.trunc(segundos%3600//60)
    segundo=math.trunc(segundos%3600%60)
    return (horas,minutos,segundo)

def control_hora(hora):
    """controla el rango de hora"""
    if 0<= hora <24:
        return True
    else: 
        return False
def control_minuto(minuto):
    """controla el rango de minutos"""
    if 0<= minuto <60:
        return True
    else: 
        return False
def control_segundo(segundo):
    """controla el rango de segundos"""
    if 0<= segundo <60:
        return True
    else: 
        return False 
def mostrar_horario(hora=0,minuto=0,segundo=0):
    """muestra en forma de renglones hora,minutos,segundo"""
    print("Hora:",hora)
    print("Minutos:",minuto)
    print("Segundos:",segundo)                       
def transformar_horario(hora=0,minuto=0,segundo=0):
    """Cambia la hora,minutos,segundo en segundos"""
    if control_hora(hora) and control_minuto(minuto) and control_segundo(segundo):
        mostrar_horario(hora,minuto,segundo)
        segsuma=hora*3600+minuto*60+segundo
        print("Equivale a: ",segsuma)
    else:
        raise ValueError("fuera de rango, Fallo la carga de horario")

def transformar_minutos(minutos):
    """transforma los minutos con coma en segundos usando la funcion"""
    return transformar_segundos(minutos*60)
def menu():
    """menu de eleccion"""
    print("Calculeitor".center(40,"-"),"""
        1- Operar en segundos
        2- Operar con Horario
        3- Operar en minutos
        cualquier otra opcion salir""")
    opcion=input("elige una opción: ")
    return opcion

def main():
    """programa principal"""
    flag=True
    while flag:
        elegido=menu()

        if elegido=="1":
            """muestra los segundos en forma hora,minutos,segundos"""
            segundos=float(input("ingrese segundos: "))
            hora,minuto,seg=transformar_segundos(segundos)
            mostrar_horario(hora,minuto,seg)
        elif elegido=="2":    
            """muestra el horario ingresado en forma hora,minutos,segundos con 
            equivalencian en segundos"""
            recibo=input("Ingrese el tiempo en HH:MM:SS ")
            recibo=recibo.split(":")
            for x in range(0,3):
                if x<len(recibo):
                    recibo[x]=int(recibo[x])
                else:
                    recibo.append(0)
            """captura el error de cargar horario fuera de la estructura 23:59:59"""            
            try:
                transformar_horario(recibo[0],recibo[1],recibo[2])
            except Exception as ex:
                print(ex)

        elif elegido=="3":
            """muestra los minutos en forma hora,minutos,segundos el sistema toma .99 como 59 segundos"""
            minutos=float(input("ingrese minutos: "))
            hora,minuto,seg=transformar_minutos(minutos)
            mostrar_horario(hora,minuto,seg)
        else:
            flag=False

main()