modelos = [
# -- 0
"""Estimado {}:
    Le damos la bienvenida al servicio.

Con afecto,
    {}""",

# -- 1
"""Hola {}, bienvenido!

Atte, {}"""
]

def generar_notas(modelo, destinatarios, remitente):
    for (i, d) in enumerate(destinatarios):
        if i > 0:
            print("---")
        print(modelo.format(d, remitente))

for (i, m) in enumerate(modelos):
    print("###### Modelo", i)
    generar_notas(m, ["<nombre>"], "<remitente>")
    print()

while True:
    modelo_selec = int(input("Seleccione un modelo: "))
    if modelo_selec>=0 and modelo_selec<len(modelos):
        break

destinatarios = []

while True:
    d = input("Ingrese un destinatario (vacio para terminar): ")
    if len(d) == 0:
        break
    destinatarios.append(d)

remitente = input("Ingrese un remitente: ")

print()
generar_notas(modelos[modelo_selec], destinatarios, remitente)
