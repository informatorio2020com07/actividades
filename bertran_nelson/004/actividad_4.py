"""
	Un programa que permita escribir varios modelos de cartas/notas
	y que después pueda seleccionar un modelo de nota, y que me generé
	varias notas reemplazando los destinatarios con una lista de nombres
	que se le pase y el nombre del remitente indicado.
    Ej:
    ----
        Estimado (nombre):
            Le damos la bienvenida al servicio.

        Con afecto,
            (nombre_remitente)
    ----
    Pasandole lista destinatarios: Juan, Sandra y Jorge.
        Y remitente Axel.
    ----
        Estimado Juan:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel
    ----
        Estimado Sandra:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel
    ----

        Estimado Jorge:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel                        
"""

print("Seleccione modelo de nota: (1 / 2) o 3 si quiere introducir su propio modelo\n"+
		"(utilice -- para salto de linea, ++ para indicar donde va el destinatario).\n"+
		"\n"+
		"1_modelo: 	'Estimado (Destinatario):\n"+
						"Le damos la bienvenida al servicio.\n"+
						"\n"+
					"Con afecto,\n"+
						"(Autor)'\n"+
						"\n"+
		"2_modelo: 'Bienvenido (Destinatario):\n"+
						"Con mucho afecto le damos la bienvenida al servicio.\n"+
						"\n"+
					"Saludos cordiales, (Autor)'\n")

opcion = input()

listaDestinatarios = []

def pideLista():
	print("Ahora ingrese una lista de destinatarios separado por coma: ")
	cadenaRemitentes = input()

	listaDestinatarios = cadenaRemitentes.split(sep=',')

	return listaDestinatarios

if opcion == "1":

	modeloUno = """
				Estimado (destinatario):
						Le damos la bienvenida al servicio.
						
					Con afecto,
						(autor)
				"""

	autor = input("Ingrese autor: ")
	listaDestinatarios = pideLista()

	modeloUno = modeloUno.replace("(autor)", autor)

	for r in listaDestinatarios:
		modeloUnoPrint = modeloUno.replace("(destinatario)", r)
		print(modeloUnoPrint)

elif opcion == "2":

	modeloDos = """
				Bienvenido (destinatario):
						Con mucho afecto le damos la bienvenida al servicio.
						
					Saludos cordiales, (autor)
				"""

	autor = input("Ingrese autor: ")

	listaDestinatarios = pideLista()

	modeloDos = modeloDos.replace("(autor)", autor)

	for r in listaDestinatarios:
		modeloDosPrint = modeloDos.replace("(destinatario)", r)
		print(modeloDosPrint)

elif opcion == "3":

	print("Escriba su modelo, recuerde usar -- para saltos de linea, ++ para indicar donde va el destinatario.")
	modeloPropio = input()
	modeloPropioSaltos = modeloPropio.replace("--", "\n")
	
	listaDestinatarios = pideLista()

	for d in listaDestinatarios:
		modeloPropioSPrint = modeloPropioSaltos.replace("++", d)
		print(modeloPropioSPrint)
		print()
