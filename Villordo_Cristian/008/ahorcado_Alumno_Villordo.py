import random
import time		
import os
print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
print("<<-*-*-*-|BIENVENIDO AL JUEGO DEL AHORCADO|-*-*-*->>")
print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
print("--------------------------")
nombre=input("ingrese su nombre: ")
os.system("cls")
while True:
	try:
		print("Hola", nombre, "eliga una opción: ")
		print("_________")
		print("|1-JUGAR|")
		print("|2-SALIR|")
		print("´´´´´´´´´")
		opcion=int(input())
		if opcion==1:
			break
		elif opcion==2:
			break
		else:
			raise NameError("ingrese una opcion (1-2)")

		break
	except:
		print(nombre,"ingrese una opcion (1-2)")

frutas=["manzana","banana","pera","naranja","mandarina","anana","ciruela","frutilla","kiwi","melon", "sandia","aguacate","coco"]
animales=["perro","gato","elefante","leon","tigre","vaca","vibora","aveztruz","cabra","cocodrilo","camaleon","flamenco","hipopotamo","jirafa"]
deportes=["futbol", "hockey", "ciclismo", "tenis", "volevoy","atletismo", "remo","natacion","buceo","basket","paracaidismo","judo","pesca","motociclismo"]

intentos=0
def muñeco(intentos):
	if intentos==1:
		print("| / |´´´´´´´´´´´+¡+")
		print("| / |            # ")
		print("| / |            # ")
		print("| / |      \\\\\\|||/// ")
		print("| / |      | -  ~ |      ")
		print("| / |     {| @  @ |}")
		print("| / |      |´ 0 ' |")
		print("| / |      | __   |")
		print("| / |      \\     /#")
		print("| / |      #|###|#")	
	if intentos==2:
		print("| / |´´´´´´´´´´´+¡+")
		print("| / |            # ")
		print("| / |            # ")
		print("| / |      \\\\\\|||/// ")
		print("| / |      | ~  ~ |      ")
		print("| / |     {| @  @ |}")
		print("| / |      |´ 0 ´ |")
		print("| / |      |  O   |")
		print("| / |      \\     /#")
		print("| / |      #|###|#")
		print("| / |      (      )")
		print("| / |      |*    *|")
		print("| / |      |   .  |")
		print("| / |      ========")		
	if intentos==3:
		print("| / |´´´´´´´´´´´+¡+")
		print("| / |            # ")
		print("| / |            # ")
		print("| / |      \\\\\\|||/// ")
		print("| / |      | `  ´ |      ")
		print("| / |     {| -  - |}")
		print("| / |      |´ 0 ´ |")
		print("| / |      | __   |")
		print("| / |      \\     /#")
		print("| / |       #|###|#")
		print("| / |       (      )")
		print("| / |     //|*    *|")
		print("| / |    // |   .  |")
		print("| / |   //  ========")
		print("| / |  ()")				
	if intentos==4:
		print("| / |´´´´´´´´´´´+¡+")
		print("| / |            # ")
		print("| / |            # ")
		print("| / |      \\\\\\|||/// ")
		print("| / |      | -  - |      ")
		print("| / |     {| >  - |}")
		print("| / |      | '0 ' |")
		print("| / |      | __   |")
		print("| / |      \\     /#")
		print("| / |       #|###|#")
		print("| / |       (      )")
		print("| / |     //|*    *|\\\\")
		print("| / |    // |   .  | ||")
		print("| / |   //  ======== ||")
		print("| / |  ()            ()")		
	if intentos==5:
		print("| / |´´´´´´´´´´´+¡+")
		print("| / |            # ")
		print("| / |            # ")
		print("| / |      \\\\\\|||/// ")
		print("| / |      | ~  - |      ")
		print("| / |     {| x  - |}")
		print("| / |      |´ 0 ' |")
		print("| / |      | __   |")
		print("| / |      \\     /#")
		print("| / |      #|###|#")
		print("| / |      (      )")
		print("| / |    //|*    *|\\\\")
		print("| / |   // |   .  | ||")
		print("| / |  //  ======== ||")
		print("| / | ()  (   _U___)()")
		print("| / |      | |")
		print("|/  |.-----' |")
		print("||  |`-------'")
	if intentos==6:
		print("| / |´´´´´´´´´´´+¡+")
		print("| / |            # ")
		print("| / |            # ")
		print("| / |      \\\\\\|||/// ")
		print("| / |      | ~  ~ |      ")
		print("| / |     {| X  X |}")
		print("| / |      |´ 0 ' |")
		print("| / |      | .-.  |")
		print("| / |      \\ \\|/ /#")
		print("| / |      #|###|#")
		print("| / |      (      )")
		print("| / |    //|*    *|\\\\")
		print("| / |   // |  .   | \\\\")
		print("| / |  //  ========  \\\\")
		print("| / |  () (   _U_  )  ()")
		print("| / |      | |   | |")
		print("|/  |     .' |   | `.")
		print("||  |    /  /'   '\\  \\")
		print("||  |   '_ '       ' _'")

def seleccion_palabra(lista):
	palabra=list(random.choice(lista))
	return palabra

def convertir_guion(palabra):
	cant=len(palabra)
	guion="_"* cant	
	return list(guion)
def cambiar_letra(letra, palabra,guion):
			letra_comparar=letra
			indice=0
			for letra in palabra:
				if letra in letra_comparar:
					guion[indice]=letra_comparar
				indice+=1
	


def ganaste():
	print("          ,,,,,")
	print("          (0 0) ")
	print("  ---oOO-- (_) ----oOO---")
	print("╔═════════════════════════╗")
	print("║*|FELICIDADES GANASTE!!|*║")
	print("╚═════════════════════════╝")
	print("  -----------------------")
	print("        |__|__|")
	print("         || || ")
	print("        ooO Ooo")
	print("la palabra era: ", ".".join(palabra))
	
def perdiste():
				print("   __^__                                      __^__")
				print("  ( ___ )------------------------------------( ___ )")
				print("   | / |                                      |\\  |")
				print("   | / |            |¡PERDISTE!|              | \\ |")
				print("   |___|                                      |___|")
				print("  (_____)------------------------------------(_____)")
				print("´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´")
				print("´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´")
				print("´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´")
				print("´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´")
				print("´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´")
				print("´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´")
				print("´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´")
				print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
				print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
				print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
				print("´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´")
				print("´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´")
				print("´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´")
				print("´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´")
				print("´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´")
				print("´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´¶¶´´´´´´´´¶¶¶¶´´")
				print("´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶´¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´")
				print("´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´")
				print("´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶´¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´")
				print("¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶´¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶")
				print("¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶´¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶")
				print("´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´´´")
				print("´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´¶¶´´´´´´´´´´´¶¶´¶¶¶´´¶¶¶¶¶¶´´´´´´´´´´")
				print("´´´´´´´´´´´´´´¶¶¶¶¶¶´¶´´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´")
				print("´´´´´´´´´´´´´´´´´´¶¶´¶´¶¶´¶¶´¶´¶¶¶¶¶¶¶´¶¶´´´´´´´´´´´´´´´´´´")
				print("´´´´´´´´´´´´´´´´¶¶¶¶´¶¶´¶´¶¶´¶´¶¶´¶´¶¶´¶¶¶¶¶´´´´´´´´´´´´´´´")
				print("´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´")
				print("´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´")
				print("´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´")
				print("´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´")
				print("´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´")
				print("´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´")
				print("´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶´´´´´´´´")
				print()
				print("la palabra era: ", ".".join(palabra))
		

os.system("cls")
if opcion == 1:
	while True:
		try:
			print("___________")
			print("|1-FRUTAS  |")
			print("|2-ANIMALES|")
			print("|3-DEPORTES|")
			print("´´´´´´´´´´´´")
			listas=(int(input("eliga una lista: ")))
			if listas==1:
				print("___________")
				print("|1-FRUTAS  |")
				print("´´´´´´´´´´´´")		
				palabra=seleccion_palabra(frutas)
				guion=convertir_guion(palabra)
				print(guion)
				break
			elif listas==2:
				print("___________")
				print("|2-ANIMALES|")
				print("´´´´´´´´´´´´")		
				palabra=seleccion_palabra(animales)
				guion=convertir_guion(palabra)
				print(guion)
				break
			elif listas==3:
				print("___________")
				print("|3-DEPORTES|")
				print("´´´´´´´´´´´´")		
				palabra=seleccion_palabra(deportes)
				guion=convertir_guion(palabra)
				print(guion)
				break
			else:
				raise NameError("ingrese una opcion (1-2-3)")
			break
		except:
				print("ha ocurrido un error, introduce bien el numero (1-2-3)")
	lista_letras=[]
	while intentos<=6:
		letra=input("ingrese una letra: ")
		
		if letra in palabra:
			os.system("cls")
			cambiar_letra(letra, palabra,guion)
			muñeco(intentos)
			print()
			print(guion)
		else:
			intentos+=1				
			os.system("cls")
			muñeco(intentos)
			print()
			print(guion)
		if letra in lista_letras:
			print("_________________________________________________")
			print("letra repetida, ya ingresaste esa letra: ", str(lista_letras))
			print("_________________________________________________")
	
		lista_letras.append(letra)

		if letra.isdigit():
			print("_____________")
			print("solo letras")
			print("_____________")

		if guion == palabra:
			os.system("cls")
			ganaste()
			break			
		letra=list(letra)
		if letra==palabra:
			os.system("cls")
			ganaste()
			break
		if intentos>6:
			perdiste()
			break
		