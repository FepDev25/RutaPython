# Diccionarios
# Almacena datos de tipo clave - valor

diccionario = {'c1': 'Valor 1',
               'c2': 'Valor 2'}

paciente = {'nombre': 'Felipe',
            'apellido': 'Peralta',
            'edad': 18,
            'altura': 1.75}

resultado = paciente['edad'] # Acceder al valor de una clave
print(resultado)

# Los diccionarios (al igual que todas las colecciones) puede almacenar a otras colecciones
super_diccionario = {'c1': 3,
                     'c2': [1,2,3,4,5],
                     'c3': {'s1': 1,
                            's2': 2},
                     'c4': 'WOW'}
for i in super_diccionario:
    print(super_diccionario[i]) # Iterar los valores de un diccionario

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper()) # Operacion con muchos metodos

dic = {1:'a', 2:'b'}
dic.keys()

diccionario = {"IDE": "Integrated Development Enviroonment",
               "OOP": "Object Oriented Programming",
               "DBMS": "Database Management System"}

for i in diccionario:
    print(diccionario[i])

diccionario = {'Uno': 1,
               'Dos': 2,
               'Tres': 3}
print(diccionario)
diccionario['Uno'] = 1.0 # Modificar los valores de una clave
diccionario['Cuatro'] = 4 # Si no existe, se crea
print(diccionario)

dic = {'c1': 100, 'c2': 200}
a = dic.popitem() # Eliminar un elemento y alamenar en una variable

print(a) # ('c2', 200)
print(type(a)) # Tupla
print(dic) # {'c1': 100}

# Distintas maneras de iterar un diccionario:
persona = {'nombre': 'Felipe',
           'edad': 18,
           'mascotas': ['Bruno', 'Perla', 'Polita', 'Mikey'],
           'happy': True}

for i in persona.keys(): # Imprime solo claves
    print(i)

for i in persona.values(): # Imprime solo valores
    print(i)

for i in persona.items(): # Imprime claves y valores
    print(i)