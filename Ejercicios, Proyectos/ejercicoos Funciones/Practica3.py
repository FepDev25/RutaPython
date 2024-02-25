def cero_consecutivos(*args):
    contador = 0
    for i in args:
        if i == 0:
            if contador == 1:
                return True
            contador += 1
        else:
            contador = 0
    return False

prueba = cero_consecutivos(5, 6, 1, 0, 0, 9, 3, 5)
print(prueba)

prueba = cero_consecutivos(6, 0, 5, 1, 0, 3, 0, 1)
print(prueba)

prueba = cero_consecutivos(8, 5, 3, 0, 1, 0, 2, 0, 0, 34)
print(prueba)

prueba = cero_consecutivos(0, 1, 0, 2, 0, 4, 5, 0, 2)
print(prueba)
