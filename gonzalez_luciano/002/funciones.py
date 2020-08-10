SEGUNDOS_EN_MINUTO = 60
SEGUNDOS_EN_HORA = SEGUNDOS_EN_MINUTO*60

def segundos_a_hms(segs):
    h = segs//SEGUNDOS_EN_HORA
    m = (segs%SEGUNDOS_EN_HORA)//SEGUNDOS_EN_MINUTO
    s = segs%SEGUNDOS_EN_MINUTO
    return (h, m, s)

def hms_a_segundos(h=0, m=0, s=0):
    return h*SEGUNDOS_EN_HORA + m*SEGUNDOS_EN_MINUTO + s