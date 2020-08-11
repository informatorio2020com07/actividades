
from actividad_2 import transformar_segundos
from actividad_2 import sumar_segundos

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

def mostrar_transformar_horario(hora=0,minuto=0,segundo=0):
    """controla y muestra la hora,minutos,segundo en segundos"""
    if control_hora(hora) and control_minuto(minuto) and control_segundo(segundo):
        mostrar_horario(hora,minuto,segundo)
        print("Equivale a: ",sumar_segundos(hora,minuto,segundo), "segundos")
    else:
        raise ValueError("fuera de rango, Fallo la carga de horario")

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
            tiempo=input("Ingrese el tiempo en HH:MM:SS ")
            recibo=[int(x) for x in tiempo.split(":")]
            """captura el error de cargar horario fuera de la estructura 23:59:59"""            
            try:
                mostrar_transformar_horario(recibo[0],recibo[1],recibo[2])
            except Exception as ex:
                print(ex)

        elif elegido=="3":
            """muestra los minutos en forma hora,minutos,segundos el sistema toma .99 como 59 segundos"""
            minutos=float(input("ingrese minutos: "))
            hora,minuto,seg=transformar_segundos(minutos*60)
            mostrar_horario(hora,minuto,seg)
        else:
            flag=False

main()