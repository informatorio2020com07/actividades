import os
def carta():
	modelos=0
	modelo=[]
	while True:
		mensaje=[]
		print("Escriba su modelo de carta,para indicar que finalizo presione: .- ",":")
		while True:
			carta=input("")
			mensaje.append(carta)
			if carta==".-":
				break
		
		mas=int(input("desea agregar otro modelo de carta?:|1-SI|2-NO|: (solo se permite ingresar 100 modelos de cartas): "))
		os.system("cls")	
		modelo.append(mensaje)
		modelos+=1
		if mas==1:		
			True
		else:
			break
	return modelo

print("====================BIENVENIDO AL SERVIVIO DE CARTAS/NOTAS====================:")
Cartas=carta()
for x in range(0,len(Cartas)):
	nombre=Cartas[x]
	print(x)
	for x in nombre:
		print(x)

sele=int(input("eliga el modelo de carta a usar: "))
os.system("cls")
while sele<10:
	destinatarios=[]
	print("Escribir el nombre de la persona a quién va dirigida la nota.")
	while True:
	    destino=input("el/la destinatario/a: ")
	    destinatarios.append(destino)
	    op=int(input("desea ingresar otro destinatario: 1-si/2-no: "))
	    os.system("cls")
	    if op==1:
	        True
	    else:
 	       break
	
	remite=input("Ingresa el nombre del remitente. Recorda que el remitente es quién escribe y envía la carta/nota: ")
	os.system("cls")

	nombre=Cartas[0]
	for destinatario in destinatarios:	    
	    for linea in nombre:
	    	remplazo = linea.replace("destinatario", destinatario).replace("remitente", remite)

	    	print(remplazo)
	    print("---------------------------------------------------------------------------------------")
	break