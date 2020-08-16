#  En otro archivo, importar las funciones creadas.
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


import re

from A002 import seconds_to_hhmmss, hhmmss_to_seconds


def preguntar_segundos():
    """Pide que ingresen segundos, y muestra el equivalente en horas, minutos y segundos"""
    segundos = int(input("Ingresar segundos: "))
    tiempo = seconds_to_hhmmss(segundos)
    print(f"En {segundos} segundos hay {tiempo[0]} horas, {tiempo[1]} minutos y {tiempo[2]} segundos.")


def preguntar_minutos():
    """Pide que ingresen minutos, y muestra el equivalente en horas, minutos y segundos"""
    minutos = int(input("Ingresar minutos: "))
    tiempo = seconds_to_hhmmss(hhmmss_to_seconds(minutes=minutos))
    print(f"En {minutos} segundos hay {tiempo[0]} horas, {tiempo[1]} minutos y {tiempo[2]} segundos.")


def validate_format(horario: str):
    """
    Valida que el 'horario' tenga el formato correcto:
    Debe ser: hh:mm:ss >>> horas(1 o mas cifras):minutos(1 o mas cifras):segundos(1 o mas cifras)
    """
    if re.match(r"\d+:\d+:\d+", horario):
        return True
    else:
        return False


def pedir_tiempo_en_string():
    """
    Pide ingresar un horario en el formato hh:mm:ss, muestra el valor ingresado, y 
    su equivalente en segundos.
    """
    while True:
        str_tiempo = input("Ingresar [hh:mm:ss]: ")
        if validate_format(str_tiempo):
            hh, mm, ss = [int(number) for number in str_tiempo.split(":")]
            hh, mm, ss = seconds_to_hhmmss(hhmmss_to_seconds(hh, mm, ss))
            print(f"Ingresado {hh} horas, {mm} minutos y {ss} segundos")
            print(f"Sumando un total de {hhmmss_to_seconds(hh, mm, ss)} segundos")
            break
        else:
            print("Formato incorrecto\n")


def main():
    preguntar_segundos()
    preguntar_minutos()
    pedir_tiempo_en_string()


if __name__ == "__main__":
    main()
