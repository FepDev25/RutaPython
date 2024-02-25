from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = uniform(1,50)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['Azul', 'Rojo', 'Verde']
aleatorio = choice(colores)
print(aleatorio)

numeros = [1, 2, 3, 4, 5]
shuffle(numeros)
print(numeros)

from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']

# Funcion de mezclar
def mezclar(lista):
    shuffle(lista)
    return lista

# Funcion Pedir al usuario que elija un numero
def probarSuerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elije un numero del 1 al 4: ")
    return int(intento) - 1

# Funcion comprobar el intento
def comprobar_intento(lista, intento):
    if lista[intento] == '-':
        print("Te toco lavar los platos")
    elif lista[intento] == '--':
        print("Te toco barrer")
    elif lista[intento] == '---':
        print("Te toco dar de comer a los perros")
    elif lista[intento] == '----':
        print("Suertudo, no haces nada.")


palitos_mezclados = mezclar(palitos)
intento = probarSuerte()
comprobar_intento(palitos_mezclados, intento)