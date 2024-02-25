# Funciones integradas, profundizacion: https://docs.python.org/3.9/library/functions.html

""" id """
nombre = "Hola"
print(id(nombre)) # 4383838576, indica la pocision en memoria de una variable
# Las rutas cambian de ubicacion constantemente

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
print('num_int', float(num_str))      # 10
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