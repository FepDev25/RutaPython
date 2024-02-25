print(2 + 3) # 5
print(3 - 2) # 1
print(3 * 2 ) # 6
print(3 / 2 ) # 1.5
print(3 ** 2 ) #9

print(9 % 2)  # 1, lo que significa encontrar el resto
print(9 // 2) # 4, lo que significa eliminar el resto

# Comentarios:
    # This is the first comment
    # This is the second comment
    # Python is eating the world

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

# Datos mas comunes:
#String:
nombre = "Felipe"
pais = "Ecuador"
oracion = "Rick y Morty es muy bello"
print(f" {nombre} {pais} {oracion} ")   

# Booleanos:
youGay = False
ChelseaBestTeam = True

# Listas
lista_1 = [0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
lista_2 = ['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
lista_3 = ['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
lista_4 = ['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float

lista_1.append(18)
print(lista_1)

for i in lista_3:
    print(i)

# Diccionarios (clave valor)

dic = {
'first_name':'Felipe',
'last_name':'Peralta',
'country':'Ecuador', 
'age':18, 
'is_married':False,
'skills':['Java', 'Python']
}

# Tuplas (no se pueden modificar como las listas)

tuple_1 = ('Felipe', 'Bruno', 'Eden', 'Abraham', 'Luka') # Names
tuple_2 = ('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets

# Set 
set_1 = {2, 4, 3, 5}
set_2 = {3.14, 9.81, 2.7} # order is not important in set

# Comprobacion tipo de datos
print(type(nombre))
print(type(youGay))
print(type(lista_1))
print(type(tuple_1))
print(type(dic))
print(type(set_1))