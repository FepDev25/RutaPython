# Tuplas: Son elementos inmutables (no puede ser modificado)
# Si se maneja por indices
# Se deben utiliar en caso de pensar que son elementos que no seran cambiados en el futuro

# Declaracion de una tupla
mi_tupla = (1, 2, 3.4)

print(mi_tupla[1])

for i in mi_tupla: # Iterar una tupla
    print(i)

mi_tupla = (1, (1, 2, 3, 4), 3.4) # Tupla con otra tupla dentro
print(mi_tupla[1][2]) #3

mi_lista = list(mi_tupla) # Transformar una tupla a una lista

tupla = (1, 2, 3, 1)
print(tupla.count(1)) # Contar un elemento dentro de la tupla
print(tupla.index(3)) # Acceder por indice

frutas = ('Naranja', 'Platano', 'Guayaba')
print(type(frutas))
print(len(frutas))
print(frutas[1])

for fruta in frutas:
    print(fruta, end=' ') # Imprimir sin salto de linea, si no que con un espacio entre frutas
print()

# En caso de editar una tupla: Cambiarlo a lista
frutas_lista = list(frutas)
frutas_lista[0] = 'Pera'
frutas = tuple(frutas_lista)
print(frutas)