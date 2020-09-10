#Un programa que permita escribir varios modelos de cartas/notas
#y que después pueda seleccionar un modelo de nota, y que me generé
#varias notas reemplazando los destinatarios con una lista de nombres
#que se le pase y el nombre del remitente indicado.
    


dest=[]
dic={"1":"nota1","2":"nota2","3":"nota3","4":"nota_propia"}

for key in dic:            #imprime el diccionario
	print(key,":",dic[key])

opcion=input("Elija una opción de nota: ")


num_destinatarios=int(input("¿Cuántos destinatarios desea ingresar?: ")) #pregunta cuantos destinatarios se ingresrán
for i in range (num_destinatarios):           #crea una lista con los nombres de los destinatarios
	nombres=input("Ingrese los nombres de los destinatarios: ")
	dest.append(nombres)


nombre_remitente=input("Ingrese nombre del remitente: ") #solicita nombre del remitenet

if opcion=="1":    #imprime el modelo eklegido a los destinatarios
	for i in range(num_destinatarios):
		print ("Estimado",dest[i])
		print("Con afecto",nombre_remitente)
elif opcion=="2":
	for i in range(num_destinatarios):
		print("Querido",dest[i])
		print("Con cariño",nombre_remitente)
elif opcion=="3":
	for i in range (num_destinatarios):
		print("Buenos días",dest[i])
		print("Con respeto",nombre_remitente)
elif opcion=="4":
	nota_usuario=input("Ingrese su modelo de nota: ")
	for i in range (num_destinatarios):
		print(dest[i],nota_usuario)
		print(nombre_remitente)

else:
	print("la opción elegida no es una opción válida")





