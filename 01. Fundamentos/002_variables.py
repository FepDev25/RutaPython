# Variables: Almacenar informacion de manera temporal.

# Nombres de variables:
"""
1. Ser especifico con su nombre
2. Al usar mas de una palabra, utilizar minusculas y guiones bajos
3. No usar acentos (tildes) o la "ñ"
4. No usar numeros al inicio
5. No utilizar simbolos o palabrs clave
6. Un nombre de variable debe comenzar con una letra o el carácter de subrayado
7. Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _)
8. Los nombres de las variables distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y FIRSTNAME) son variables diferentes)
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

## Declaracion de variables multiples
mascota1, mascota2, mascota3, mascota4, mascota5 = "Bruno", "Mikey", "Juancho", "Polita", "Perla"
print(f"{mascota1} {mascota2} {mascota3} {mascota4} {mascota5} ") 
print()


miVariableNombre = 'Felipe'
print(miVariableNombre)

# Tipado Dinamico
miVariable = 'Hola'
print(type(miVariable)) # type(): Regresa el tipo de dato
miVariable = 81
print(type(miVariable))

# Ejercicio
nombre = 'Felipe'
phone = 2875755
mail = 'dperalta@gmail.com'
print(nombre)
print(phone)
print(mail)

edad = 18
print(edad)

edad2 = 25 + edad
print(edad2)

# nombre = input('Dime tu nombre: '), Los inputs(entradas de usuario), se pueden almacenar en variables.
print(nombre)