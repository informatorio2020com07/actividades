
def dibujar(intento):
	muñeco=["O","|","/","\\","Ø"," "]
	if intento ==1:
		print("     {}   ".format(muñeco[0]))
	elif intento==2:
		print("     {}   ".format(muñeco[0]))
		print("    {}{}{} ".format(muñeco[5],muñeco[1],muñeco[5]))
	elif intento==3:
		print("     {}   ".format(muñeco[0]))
		print("    {}{}{} ".format(muñeco[2],muñeco[1],muñeco[5]))
	elif intento==4:
		print("     {}   ".format(muñeco[0]))
		print("    {}{}{} ".format(muñeco[2],muñeco[1],muñeco[3]))
	elif intento==5:		
		print("     {}   ".format(muñeco[0]))
		print("    {}{}{} ".format(muñeco[2],muñeco[1],muñeco[3]))
		print("    {} {}  ".format(muñeco[2],muñeco[5]))
	elif intento==6:		
		print("     {}   ".format(muñeco[0]))
		print("    {}{}{} ".format(muñeco[2],muñeco[1],muñeco[3]))
		print("    {} {}  ".format(muñeco[2],muñeco[3]))
	elif intento==7:	
		print("     {}   ".format(muñeco[4]))
		print("    {}{}{} ".format(muñeco[2],muñeco[1],muñeco[3]))
		print("    {} {}  ".format(muñeco[2],muñeco[3]))

