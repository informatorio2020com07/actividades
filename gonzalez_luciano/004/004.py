modelos = [
# modelos de prueba

# -- 0
"""Estimado <des>:
    Le damos la bienvenida al servicio.

Con afecto,
    <rem>
""",

# -- 1
"""Hola <des>, bienvenido!

Atte, <rem>
"""
]

def mostrar_modelos():
    print()
    for i, m in enumerate(modelos):
        if i > 0:
            print("-"*10 + "\n")
        print("#### Modelo ", i, ":", sep="")
        print(m)

def leer_modelo():
    print("-"*10)
    print("Escriba su modelo.")
    print("Puede utilizar varias lineas.")
    print("Ingrese una linea en blanco para terminar.")
    print("Utilize <des> donde quiere que aparezca el nombre del destinatario.")
    print("Y similarmente <rem> para el remitente.")

    lineas = []
    while True:
        linea = input("> ")
        if len(linea) == 0:
            break
        lineas.append(linea + "\n")
    modelos.append("".join(lineas))

def generar_notas():
    while True:
        nro_modelo = int(input("Ingrese un numero de modelo (del 0 al {}): ".format(len(modelos)-1)))
        if nro_modelo>=0 and nro_modelo<len(modelos):
            modelo = modelos[nro_modelo]
            break

    destinatarios = []
    while True:
        dest = input("Ingrese un destinatario (vacio para terminar): ")
        if len(dest) == 0:
            break
        destinatarios.append(dest)

    remitente = input("Ingrese un remitente: ")

    print()
    for i, d in enumerate(destinatarios):
        if i > 0:
            print("-"*10 + "\n")
        print(modelo.replace("<des>", d).replace("<rem>", remitente))

while True:
    print("1. Ver modelos")
    print("2. Ingresar modelo")
    print("3. Generar nota")
    print("4. Salir")

    while True:
        opcion = int(input("Ingrese una opción: "))
        if opcion>=1 and opcion<=4:
            break

    if opcion == 1:
        mostrar_modelos()
    elif opcion == 2:
        leer_modelo()
    elif opcion == 3:
        generar_notas()
    else:
        break
