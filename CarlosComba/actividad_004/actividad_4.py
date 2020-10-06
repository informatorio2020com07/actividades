import sys
import mysql.connector
class Nota():
    def __init__(self,titulo,nota):
        self.__titulo=titulo
        self.__nota=nota

    def get_titulo(self):
        return self.__titulo

    def get_nota(self):
        return self.__nota

def ingresar_nota():
    print("ingrese su nota  en el nombre de las persona ingrese 'destinatario' y 'remitente'\
 para salir escriba termine solo")
    """Recibe la nota en oraciones"""
    lista_renglones=[]
    titulo=input("ingrese Titulo: ")
    while True:
        print("Linea:",end=" ")
        renglon=input("")
        if renglon.lower()=="termine":
            break
        while len(renglon)>399:
                if len(renglon[0:renglon.find(".")+1]) < 399:
                    lista_renglones.append(renglon[0:renglon.find(".")+1])
                    renglon=renglon[renglon.find(".")+1:len(renglon)-1]
                elif len(renglon[0:renglon.find(",")+1]) < 399:
                    lista_renglones.append(renglon[0:renglon.find(",")+1])
                    renglon=renglon[renglon.find(",")+1:len(renglon)-1]                     
                else:
                     lista_renglones.append(renglon[0:399])
                     renglon=renglon[399:len(renglon)-1]
        lista_renglones.append(renglon)
    nota=Nota(titulo, lista_renglones) 
    return nota
        
    

def ingresar_personas():
    """recibe los destinatarios"""
    lista=[]
    while True:
        destinatario=input("Ingrese la persona destinatario, ingrese un numero \
para salir: ")
        print("")
        if destinatario.isnumeric():
            break
        lista.append(destinatario)
    """recibe el remitente"""     
    remitente=input("Ingrese la persona remitente: ")    
    return lista,remitente

def cambiar_mensaje(nota_entrante,destinatario,remitente):
    """cambiar destinatario y remitente"""
    nota_recibida=nota_entrante.copy()
    for y,x in enumerate(nota_recibida):
        nota_recibida[y]=x.replace("destinatario",destinatario).replace("remitente",remitente)        
    return nota_recibida

def cargar_nota():
    """cargar archivo nota"""
    notas=[]
    conexion1=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="nota"
        )
    cursor=conexion1.cursor()
    """cursor de titulo"""
    query="SELECT titulo,id_nota FROM titulo"
    cursor.execute(query)
    identificador=cursor.fetchall()
    """cursor de renglón"""
    query="SELECT id_nota,renglones FROM renglones"
    cursor.execute(query)
    archi=cursor.fetchall()
    """devuelve una lista de dato clase nota"""
    for titulo,id_nota in identificador:
        renglones=[]
        for x in archi:
            if x[0]==id_nota:
                renglones.append(x[1])
        notas.append(Nota(titulo,renglones))
    return notas

def buscar_por_nombre(nota):
    """busca"""
    notas=cargar_nota()
    for note in notas:
        if note.get_titulo()==nota.get_titulo():
            return note

def guardar_nota(nota):
    """conecta con mysql"""
    conexion1=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="nota"
        )
    cursor=conexion1.cursor()
    
    """crea el titulo si no existe"""
    query="INSERT INTO titulo(titulo) SELECT(%s) FROM dual WHERE \
NOT EXISTS(SELECT titulo FROM titulo WHERE titulo=%s)LIMIT 1"
    dato=(nota.get_titulo(),nota.get_titulo())
    cursor.execute(query,dato)
    conexion1.commit()
    
    """trae el identificador del titulo"""
    query="SELECT id_nota FROM titulo where titulo=%s"
    dato=(nota.get_titulo(),)
    cursor.execute(query,dato)
    id_nota_titulo=cursor.fetchall()
    
    """busca el identidicador dentro de los renglones"""
    query="SELECT id_nota FROM renglones where id_nota=%s"
    dato=id_nota_titulo[0]
    cursor.execute(query,dato)
    id_nota_renglones=cursor.fetchall()
    
    """si no existe nota con ese identificador la crea"""
    if id_nota_renglones == []:
        query="INSERT INTO renglones(id_nota,renglones) values (%s,%s)"
        nota_texto=nota.get_nota()
        for renglon in nota_texto:
            datos=(id_nota_titulo[0][0],renglon)
            cursor.execute(query,datos)
        conexion1.commit()
        return True
    else:
        print("nota con ese nombre existe") 
        return False

def elegir_predefinido():
    try:
        lista_nota=cargar_nota()
    except Exception as ex:
        print("hola")
        print(ex)
    
    print("")
    for lis in lista_nota:
        mostrar_nota(lis)
    print("")

    titulo=input("titulo elegido: ").lower()
    for nota in lista_nota:
        if nota.get_titulo()==titulo:
            nota_elegida=nota
            break
    return nota_elegida

def mostrar_nota(tipo_nota):
    titulo=tipo_nota.get_titulo()
    lista=tipo_nota.get_nota()
    print("")
    print("----")
    print("\t",titulo.upper())
    print("")
    for x,linea in enumerate(lista):
        if x==0:
            print("    ",linea)
        elif x==len(lista)-1:
            print("    ",linea)
        else:
            print("  ",linea) 


def main():
    print("1- Mensaje predefinido")
    print("2- Mensaje propio")
    print("sali con cualquier otra opción")
    opcion=int(input("Ingrese Opción:"))
    if opcion == 1:
        print("Modelos de nota")
        nota=elegir_predefinido()    
    elif opcion == 2:
        print("Manda tu mensaje")       
        print("")
        nota=ingresar_nota()
        """si la nota existe entrega la copia existente"""
        if not guardar_nota(nota):
            nota=buscar_por_nombre(nota)
    else:
        sys.exit(0)

    destinatarios,remitente=ingresar_personas()
    for destinatario in destinatarios:
        mostrar_nota(Nota(nota.get_titulo(),cambiar_mensaje(nota.get_nota(),destinatario,remitente)))

main()