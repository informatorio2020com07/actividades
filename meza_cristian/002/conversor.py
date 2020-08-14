def segundos_HMS(segundos):
    hs = segundos // 3600
    min = (segundos % 3600) // 60
    seg = (segundos % 3600) % 60
    return (hs, min, seg)


def total_segundos(h=00, m=00, s=00):
    segundostotales = (h * 3600) + (m * 60) + s
    return segundostotales
