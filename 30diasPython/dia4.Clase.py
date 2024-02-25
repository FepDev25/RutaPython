# Cadenas

"""Los textos son un tipo de datos de cadena. Cualquier tipo de datos escrito como texto es una cadena. Todos los datos entre comillas
simples, dobles o triples son cadenas. Existen diferentes métodos de cadena y funciones integradas para manejar tipos de datos de 
cadena. Para verificar la longitud de una cadena, use el método len()."""

nombre = 'Felipe'
apellido = "Peralta"
mascota = """Bruno"""
print(len(nombre)) 
print(f"{nombre} {apellido} tiene como mascota a {mascota}")

letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13, Cuentan espacios y caracteres especiales
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# Cadenas multilinea

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

info = """Me llamo Felipe Peralta
y estouy cursando el reto de
30 dias con Python."""
print(info)

# Concatenacion de cadenas:

first_name = 'Felipe'
last_name = 'Peralta'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Felipe Peralta
# Checking the length of a string using len() built-in function
print(len(first_name))  # 6
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 14

# Secuencias de escape en cadenas
"""En Python y otros lenguajes de programación \ seguido de un carácter es una secuencia de escape. Veamos los caracteres de escape más comunes:

\n: nueva línea
\t: Tabulador significa (8 espacios)
\\: barra invertida
\': Una frase (')
\": comillas dobles (")"""

print('Tabla de clasifiacion que espero tenga la Premier League 2023') # line break
print('Pos\tEquipo\t\tPuntos') # adding tab space or 4 spaces 
print('1. \tChelsea FC\t102')
print('2. \tManchester City\t89')
print('3. \tArsenal FC\t82')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# Formato de cadena estilo antiguo:

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Nuevo formato

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Formato aun mas nuevo. Interpolacion de cadenas

first_name = 'Felipe'
last_name = 'Peralta'
language = 'Python'
formated_string = f'I am {first_name} {last_name}. I learn {language}'
print(formated_string)

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Acceso a cadenas por su indice:

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
last_index = language[-1]
print(last_letter) # n

# Dividir cadenas en subcadenas

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Invertir una cadena

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Cortar caracteres con salto diferente de uno
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

# Metodos de las cadenas:

#capitalize (): convierte el primer carácter de la cadena en letra mayúscula
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): devuelve ocurrencias de subcadena en cadena, cuenta(subcadena, inicio=.., final=..). El inicio es una indexación inicial para contar y el final es el último índice para contar.
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

#termina con (): comprueba si una cadena termina con un final específico
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

#expandtabs (): reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

#find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

#rfind(): Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

#index (): devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de cadena - 1). Si no se encuentra la subcadena, genera un valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error

# rindex(): Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de la cadena - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error#

#isalpha(): comprueba si todos los elementos de cadena son caracteres alfabéticos (az y AZ)

#isdecimal(): comprueba si todos los caracteres de una cadena son decimales (0-9)

#isdigit(): comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para números)

#isnumeric(): comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo acepta más símbolos, como ½)3

#islower(): Comprueba si todos los caracteres del alfabeto en la cadena están en minúsculas

#isupper(): Comprueba si todos los caracteres del alfabeto en la cadena están en mayúsculas

#join(): Devuelve una cadena concatenada
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

#replace (): reemplaza la subcadena con una cadena dada
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

#split (): divide la cadena, utilizando la cadena dada o el espacio como separador
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

#title (): devuelve una cadena de título en mayúsculas
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

#comienza con (): comprueba si la cadena comienza con la cadena especificada
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False