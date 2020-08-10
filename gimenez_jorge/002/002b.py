import aaa

segs = int(input("Cuantos segundos: "))

print(aaa.segundero(segs))


mins = int(input("Cuantos minutos: "))

segundos = aaa.horatero(minutos=mins)

print(aaa.segundero(segundos))


tiempo = input("horas:minutos:segundos ")
h,m,s = tiempo.split(":")
h = int(h)
m = int(m)
s = int(s)
print("Horas: ", h)
print("Minutos: ", m)
print("Segundos: ", s)
print("Equivale a: ", aaa.horatero(h, m, s))