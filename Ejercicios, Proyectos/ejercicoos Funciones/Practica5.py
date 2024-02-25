from random import *
# Ej 1
def lanzar_dados():
    dado1 = randint(1, 7)
    dado2 = randint(1, 7)
    return (dado1, dado2)


def evaluar_jugada(dado1, dado2):
    if dado1 + dado2 <= 6:
        return f"La suma de tus dados es {dado1 + dado2}. Lamentable"
    elif 6 < dado1 + dado2 < 10:
        return f"La suma de tus dados es {dado1 + dado2}. Tienes buenas chances"
    elif dado1 + dado2 >= 10:
        return f"La suma de tus dados es {dado1 + dado2}. Parece una jugada ganadora"