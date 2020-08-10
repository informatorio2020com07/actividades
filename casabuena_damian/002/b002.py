def pasar_a_hhmmss(segundos):
    horas=segundos//3600
    segs=segundos%3600
    minutos=segs//60
    segundos=segs%60
    return horas, minutos, segundos

def pasar_a_segundos(horas=0,minutos=0,segundos=0):
    c_segs=(horas*3600)+(minutos*60)+segundos
    return c_segs