import os
"""004-

    Un programa que permita escribir varios modelos de cartas/notas
y que después pueda seleccionar un modelo de nota, y que me generé
varias notas reemplazando los destinatarios con una lista de nombres
que se le pase y el nombre del remitente indicado."""
print("¡Hola! Bienvenido/a a nuestro servicio de cartas y notas.")
print("Seleccioná un modelo de carta/nota de los siguientes que aparecen")
mensajes="""
---------------------------------------------------------------------------------------------------------------
1-Querido/a (nombre del/la destinatario/a):
        Te envío esta carta desde Chaco para contarte lo bien que la estoy pasando con mi familia.
   
    Con mucho afecto,
        (nombre del/la remitente)

---------------------------------------------------------------------------------------------------------------
2-Sr./Sra. (nombre del/la destinatario/a):
        Tengo el agrado de comunicarle que su solicitud a las becas "Fullstack Desarrollador" ha sido aprobada.
   
    Sin más, saludo atte.,
        Sr./Sra. (nombre del/la remitente)

----------------------------------------------------------------------------------------------------------------
3- Estimado/a (nombre del/la destinatario/a):
            Le damos la bienvenida al servicio.

        Con afecto,
            (nombre del/la remitente)
----------------------------------------------------------------------------------------------------------------"""
print(mensajes)
opc=int(input())
os.system("cls")
destinatarios=[]
print("Escribir el nombre de la persona a quién va dirigida la nota.")
while True:
    destino=input("el/la destinatario/a: ")
    destinatarios.append(destino)
    op=int(input("desea ingresar otro destinatario: 1-si/2-no"))
    if op==1:
        True
    else:
        break
os.system("cls")
remite=input("Ingresa el nombre del remitente. Recorda que el remitente es quién escribe y envía la carta/nota: ")
if opc == 1:
    for x in range(0,len(destinatarios)):
        mens1="""
        -----------------------------------------------------------------------------------------------------------------
            -Querido/a {}:
                     Te envío esta carta desde Chaco para contarte lo bien que la estoy pasando con mi familia.
                    
                Con mucho afecto,
                        {}""".format(destinatarios[x],remite)
        print(mens1)
elif opc==2:
    for x in range(0,len(destinatarios)):
        mens2="""
        ------------------------------------------------------------------------------------------------------------------
            -Sr./Sra. {}:
                 Tengo el agrado de comunicarle que su solicitud a las becas "Fullstack Desarrollador" ha sido aprobada.
                  
                Sin más, saludo atte.,
                     Sr./Sra. {}""".format(destinatarios[x],remite)
        print(mens2)
else:
    for x in range(0,len(destinatarios)):
        mens3="""
        -------------------------------------------------------------------------------------------------------------------
            -Estimado/a {}:
                Le damos la bienvenida al servicio.
    
                Con afecto,
                    {}""".format(destinatarios[x],remite)
        print(mens3)

"""Ej:
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
    ----"""

