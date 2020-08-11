import os

tipocarta=["""Estimado {} :
			    DEBERA PRESENTARSE EN NUESTRAS OFICINAS EL DIA JUEVES PROXIMO.

			    SIN MAS, 
			    		{}""",
			""" POR LA PRESENTE, COMUNICAMOS AL SR {}, QUE ESTAN A DISPOSICION LOS ARTICULOS
	ENCARGADOS

 				CORDIALMENTE, {}"""    		
]

def imprimir_carta(lista_destinatarios, tipo, remitente):
	os.system("cls")
	for destinatario in lista_destinatarios:

			print(tipocarta[tipo].format(destinatario,remitente))
			print("-"*79)



def seleccionar_tipo(tipocarta):
	
	if len(tipocarta) > 0:
		for i in range(len(tipocarta)):	
			print("{} - {}".format(i,tipocarta[i]))
		tipo = int(input("Ingrese tipo :"))
		if 0 <= tipo < len(tipocarta):
			return tipo
		else:
			seleccionar_tipo(tipocarta)



lista_destinatarios=["Juan", "Jose", "Fernando"]
remitente = "Andres"

imprimir_carta(lista_destinatarios, seleccionar_tipo(tipocarta), remitente)