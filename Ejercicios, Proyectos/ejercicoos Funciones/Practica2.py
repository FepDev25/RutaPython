def no_repetidas_ordenadas(palabra):
    mi_set = set()
    for i in palabra:
        mi_set.add(i)
    lista = list(mi_set)
    lista.sort()
    return lista

prueba = no_repetidas_ordenadas('entretenido')
print(prueba)

prueba = no_repetidas_ordenadas('hipopotamo')
print(prueba)
