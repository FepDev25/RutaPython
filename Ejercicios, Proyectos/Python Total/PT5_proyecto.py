from random import choice

def seleccionar_palabra(lista):
    """
    Seleccionar una palabra del banco de palabras.
    """
    return choice(lista)

def mostrar_guiones(palabra):
    variable = '_' * len(palabra)
    lista_aux = []
    for i in variable:
        lista_aux.append(i)
    mostrar = ' '.join(lista_aux)
    print(f"La palabra a adivinar es: {mostrar}")
    return variable

def pedir_letra():
    """
    El usuario ingresa una letra
    """
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    letra = ' '
    while letra not in abecedario or len(letra) != 1:
        letra = input("Ingrese una letra: ").lower()
        if letra not in abecedario or len(letra) != 1:
            print("Ingrese una letra valida!")
    return letra

def validar_letra(palabra, letra, guiones, vidas, fallos):
    palabra.lower()
    if letra in palabra:
        print('Correcto!')
        indice = palabra.index(letra)
        lista_aux = []
        for i in guiones:
            lista_aux.append(i)
        lista_aux[indice] = letra
        respuesta = ''.join(lista_aux)

        lista_aux = []
        for i in palabra:
            lista_aux.append(i)
        lista_aux[indice] = '0'
        palabra = ''.join(lista_aux)
    else:
        vidas -= 1
        fallos.append(letra)
        print(f"Lista de fallos: {fallos}")
        if vidas == 0:
            print("Perdiste!")
        elif vidas == 1:
            print(f"Te queda {vidas} vida!")
        else:
            print(f"Te quedan {vidas} vidas!")
        respuesta = guiones

    return vidas, respuesta, palabra, fallos

def juego_ahorcado(lista):
    vidas = 6
    lista_fallos = []
    palabra = seleccionar_palabra(lista)
    aux_palabra = palabra
    guiones = mostrar_guiones(palabra)
    while vidas > 0:
        print('*'*20)
        letra = pedir_letra()
        vidas, guiones, palabra, lista_fallos = validar_letra(palabra, letra, guiones, vidas, lista_fallos)

        lista_aux = []
        for i in guiones:
            lista_aux.append(i)
        mostrar = ' '.join(lista_aux)

        if vidas > 0:
            print(f'Palabra: {mostrar}')

        if aux_palabra == guiones:
            print('Ganaste!')
            break
    if vidas <= 0:
        print(f"La palabra era {aux_palabra}")

lista = ['elefante', 'gato', 'perro', 'casa', 'musica', 'programacion', 'listas', 'juego','chelsea', 'koala', 'dinosaurio',
         'elegante','tramposo', 'vehiculo', 'tiburon', 'remigio']
juego_ahorcado(lista)