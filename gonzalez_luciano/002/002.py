from funciones import segundos_a_hms, hms_a_segundos

segundos = int(input("Ingrese una cantidad de segundos: "))
hms = segundos_a_hms(segundos)
print("{} segundos = {}h:{}m:{}s".format(segundos, hms[0], hms[1], hms[2]))
print()


minutos = int(input("Ingrese una cantidad de minutos: "))
hms = segundos_a_hms(minutos*60)
print("{} minutos = {}h:{}m:{}s".format(minutos, hms[0], hms[1], hms[2]))
print()


s = input("Ingrese una cantidad de tiempo en formato hh:mm:ss (por ejemplo, 11:22:33): ")
hms = s.split(":")
h = int(hms[0])
m = int(hms[1])
s = int(hms[2])
print("Horas:", h)
print("Minutos:", m)
print("Segundos:", s)
print("Equivale a:", hms_a_segundos(h, m, s))