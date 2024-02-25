# Listas: Colecccion que nos permite almacenar datos de todo tipo.
empty_list = [] # this is an empty list, no item in the list

mi_lista = [3, 4, 78 ,"Juan"] # Declaracion de lista
mi_otra_lista = [2, 4, 'Pedro', 5.3]

super_lista = mi_lista + mi_otra_lista # Concatenar una lista
print(super_lista)

# Los indices nos permiten acceder a los datos: 
print(mi_lista[1]) 
print(mi_lista[:4])
print(mi_lista[1:])

letras = ["A", "B", "C", "D"]
print(letras[0])
letras[3] = "d" # Cambiar / editar el elmento de una lista por su indice
print(letras)

letras.pop() # Eliminar el ultimo elemento
print(letras)

letras.pop(0) # Eliminar indice indicado
print(letras)

letras = ["B", "A", "D", "C"]
print(letras)
letras.sort() # Ordenar la lista
print(letras)

letras.reverse() # Revertir el orden de la lista
print(letras)

letras = ["B", "A", "D", "C"]
letras.clear() # Eliminar todos los elementos
print(letras)

letras = ["B", "A", "D", "C"]
letras.insert(1,"Hola") # Agregar un elemento, indicando el indice
print(letras)

letras = ["B", "A", "D", "C"]
letras.remove("C") # Eliminar indicando el elemento
print(letras)



nombres = ['Felipe', 'Juan', 'Pedro', 'Joaquin']
print(nombres)

for i in nombres: # Iterar una lista
    print(i)

# Imprimir por indices:
print(nombres[2]) 
print(nombres[1:3])

lista = [1, 3, 2, 4]
lista[1] = 2
lista[2] = 3
print(lista)

# Imprimir el tipo de dato
print(len(lista))

numeros = [3, 4, 5]
print(numeros)
numeros.append(6)
print(numeros)
numeros.insert(1,8)
print(numeros)

numeros = [1, 2, 3, 4]
numeros.pop()
print(numeros)
numeros.remove(1)
print(numeros)
del numeros[0]
print(numeros) 