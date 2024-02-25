# Set: Coleccion que no posee indices (no mantieneun orden)
# Sus elementos no pueden repetirse
# Se puede modificar

# Declaracion de set:
mi_set = {1, 2, 3, 4}
print(mi_set)

mi_otro_set = {1, 2, 3, 4, (1, 2, 3)} # Set con tupla
print(mi_otro_set)

s1 = {1, 2, 3}
s2 = {13, 14, 5}

s3 = s1.union(s2) # Unir dos sets
print(s3)

s3.add(6) # Agregar a un set
print(s3)

s3.remove(1) # Eliminar un elemento (no po su indice, por su valor)
print(s3)

s3.pop() # Elimina un elemento ala azar
print(s3)

planetas = {'Marte', 'Tierra', 'Venus'}
print(planetas)

print(len(planetas)) # Len del set

planetas.add('Jupiter')
print(planetas)

planetas.remove('Venus')
print(planetas)

# Discard no regresa un error en caso de que el elemento no se encuentre en el set (remove si lo hace)
planetas.discard('Marte') 
print(planetas)