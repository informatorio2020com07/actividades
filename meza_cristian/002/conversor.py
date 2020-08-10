import datetime


def segundos_HMS(segundos):
    return str(datetime.timedelta(seconds=segundos))


def total_segundos(h=0,m=0,s=0):
    segundostotales = (h * 3600) + (m * 60) + s
    return segundostotales
