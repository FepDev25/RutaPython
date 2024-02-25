# Los strings son un tipo de dato donde se almacenan cadenas de texto


texto = "texto de Felipe"

resultado = texto.upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto[10].upper()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("e")
print(resultado)

a = 'Aprender'
b = 'Python'
c = 'es genial'

e = " ".join([a,b,c])
print(e)

texto = 'Hola Dragon'
resultado = texto.replace("Dragon","Loba")
print(resultado)

texto = "ABCDEFGHIJKLMNOP"
print(texto[2])
print(texto[2:5])
print(texto[2:11:2])
print(texto[2:])
print(texto[:5])
print(texto[::3])
print(texto[::-1])

nombre1 = "Kari"
nombre2 = "na"
print(nombre1 + nombre2)

poema = """Mis pequenos
peces blancos como 
si hirviera en el agua"""
print(poema)
print("peces" in poema)
print("sol" not in poema)

string = "Hola Mundo!"
print(len(string))

print("Hola"*6)

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