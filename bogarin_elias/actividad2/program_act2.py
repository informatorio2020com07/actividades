from actdos import cantsegs, canthoras
segs=int(input("Cuantos segundos:  "))
print(cantsegs(segs))
#pasa de segundos a minutos y segundos

mins=int(input("Cuantos minutos:  "))
segundos= (canthoras(minutos=mins))
print(cantsegs(segundos))
#pasa a mins,seg,hors

tiempo= input(" : : ")
h,m,s=tiempo.split(":")
h= int(h)
m=int(m)
s=int(s)
print("Horas: ", h)
print ("minutos: ", m)
print("segundos: ", s)
#pasa a imprimir HH:MM:SS
print("Vale: ",canthoras(h,m,s))
#suma las cantidades