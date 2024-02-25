# Funciones integradas, profundizacion: https://docs.python.org/3.9/library/functions.html

""" Len """
nombre = "Felipe"
print(len(nombre)) # 6, len devuelve el numero de caracteres

nombres = ["Pedro", "Juan", "Tomas"]
print(len(nombres)) # 3
print()

""" Type """
print(type(nombre)) # <class 'str'>, type devuelve el tipo de dato

print(type([1,2,3,4,5])) # <class 'list'>
print()

""" CASTING"""
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

""" Str """
x = 9
x_string = str(x) # Combierte a str
print(f"{type(x)}  {type(x_string)}") # <class 'int'>  <class 'str'>
print()

""" Int """
x = "10"
x_int = int(x) # Combierte a int
print(f"{type(x)}  {type(x_int)}") # <class 'str'>  <class 'int'>
print()

""" Float """
x = 9
x_float = float(x) # Combierte a float
print(f"{type(x)}  {type(x_float)}") # <class 'int'>  <class 'float'>
print()

""" Help """
help("keywords")
"""
        Here is a list of the Python keywords.  Enter any keyword to get more help.

        False               class               from                or
        None                continue            global              pass
        True                def                 if                  raise
        and                 del                 import              return
        as                  elif                in                  try
        assert              else                is                  while
        async               except              lambda              with
        await               finally             nonlocal            yield
        break               for                 not                 
"""

""" Min y Max """
lista = [ 25,21,13,67,1,22]

print(max(lista)) # 67
print(min(lista)) # 1

print(sum(lista)) # 149, la sumade todos los numeros 
print()

#*************** VARIABLES ************

"""
Reglas de nombres de variables de Python

Un nombre de variable debe comenzar con una letra o el carácter de subrayado
Un nombre de variable no puede comenzar con un número
Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _)
Los nombres de las variables distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y FIRSTNAME) son variables diferentes)
""" 

## Variables validas:
firstname = "Diego"
lastname = "Peralta"
age = 18

## Variables invalidas:
# first-name
# first@name
# first$name
# num-1
# 1num
 
# Variables in Python
first_name = 'Felipe'
last_name = 'Peralta'
country = 'Ecuador'
city = 'Cuenca'
age = 18
is_married = False
skills = ['HTML', 'CSS', 'JS', 'Java', 'Python']
person_info = {
   'firstname':'Felipe',
   'lastname':'Peralta',
   'country':'Ecuador',
   'city':'Cuenca'
   }

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument
print()

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
print()

## Declaracion de variables multiples
mascota1, mascota2, mascota3, mascota4, mascota5 = "Bruno", "Mikey", "Juancho", "Polita", "Perla"
print(f"{mascota1} {mascota2} {mascota3} {mascota4} {mascota5} ") 
print()

## Obtener datos ingresados por un usuario:

first_name = input('What is your name: ')
age = input('How old are you? ')
print(f"name: {first_name}")
print(f"age: {age}")
print()

## Mas comprobaciones de tipos de datos:
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
print()