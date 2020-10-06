
def mostrar_palabra(palabra,letra,resp):
	contar=0
	#primera letra
	print(" {}".format(palabra[0]),end="")
	for x in palabra[1:len(palabra)-1]:
		contar+=1
		if x ==letra:
			resp.pop(contar-1)
			resp.insert(contar-1,x)
			#letra encontrada
			print("{}".format(resp[contar-1]),end="")
		else:
			#vacios y letras en lista
			print("{}".format(resp[contar-1]),end="")	
	#ultima letra
	print("{}".format(palabra[len(palabra)-1]))
	return resp
