import random

plantilla = """
______
|    {}
|   {}{}{}
|    {}
|   {} {}
|
"""

palabras = [
    "casa",
    "auto",
    "escuela",
    "telefono"
]

def mostrar_estado(palabra, letras, vidas):
    print(plantilla.format(
        "O" if vidas<7 else "",
        "/" if vidas<6 else "",
        "|" if vidas<5 else "",
        "\\" if vidas<4 else "",
        "|" if vidas<3 else "",
        "/" if vidas<2 else "",
        "\\" if vidas<1 else ""))

    letras = letras.copy()
    for letra in palabra:
        if letras[letra] > 0:
            print(letra+" ", end="")
            letras[letra] -= 1
        else:
            print("_ ", end="")
    print("\n")

def jugar():
    vidas = 7
    aciertos = 0
    palabra = random.choice(palabras)

    letras = {}
    for l in palabra:
        letras[l] = 0

    mostrar_estado(palabra, letras, vidas)

    while True:
        letra = input("Ingrese una letra: ")
        if (len(letra) < 1) or (not letra[0].isalpha()):
            continue
        letra = letra[0]
        if (letra in palabra) and (letras[letra] < palabra.count(letra)):
            letras[letra] += 1
            aciertos += 1
        else:
            vidas -= 1

        mostrar_estado(palabra, letras, vidas)
        
        if vidas == 0:
            print("Perdiste!\n"
                  "La palabra era: "+palabra)
            return
        elif aciertos == len(palabra):
            print("Ganaste!")
            return

def menu_principal():
    print("Bienvenido!")
    while True:
        print("\n####\n"
              "¿Que desea hacer?\n"
              "1 - Jugar\n"
              "2 - Salir\n"
              "####\n")
        while True:
            opcion = input("Ingrese una opción: ")
            if len(opcion) < 1:
                continue
            if opcion[0] == "1":
                jugar()                
                break
            elif opcion[0] == "2":
                print("Hasta luego!")
                return

menu_principal()