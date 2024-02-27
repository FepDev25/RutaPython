"""*******************************Prints*******************************"""
print("Hola Mundo")
print("Me llamo Felipe")

"""*******************************Variables*******************************"""
nombre = "Felipe"
edad = 19
apellido = 'Peralta'
print(f"{nombre} {apellido}, y tiene {edad}")

l1, l2, l3 = 'Python','Java', "JavaScript"
print(l2) #Java
print(l1) #Python
print(l3) #JavaScript

print(type("Hola")) #<class 'str'>
print(type(edad)) #<class 'int'>
# print(edad + "10") Error
print(edad + 10) # 29
print("22" + '2') # 222

"""*******************************Operaciones Basicas*******************************"""
x = 10
y = -9
print(x + y) # 1
print(f"La suma de {2} + {4} es {2+4}") # La suma de 2 + 4 es 6

x = 10
y = 5
print(f"Suma: {x} + {y} = {x+y}")
print(f"Resta: {x} - {y} = {x-y}")
print(f"Multiplicacion: {x} * {y} = {x*y}")
print(f"Division: {x} / {y} = {x/y}")
print(f"Potencia: {x} ** {y} = {x**y}")
print(f"Igualdad: {x} == {y} = {x==y}")
print(f"Residuo: {x} % {y} = {x%y}")
x = 19
y = 5
print(f"Division entera: {x} // {y} = {x//y}")

"""*******************************Tipos de Datos*******************************"""
x = 7
print(type(x))

nombre = 'Felipe'
print(type(nombre))

casado = False
print(type(casado))

promedio = 6.5
print(type(promedio))

mascotas = ['Mikey', 'Bruno', 'Polita', 'Perlita', 'Actros']
print(type(mascotas))

diccionario = {'nombre':'Felipe','edad':18}
print(type(diccionario))

frutas = ('manzana', 'pera', 'mandarina', 'melon')
print(type(frutas))

vocales = {'a', 'b', 'c', 'd', 'e'}
print(type(vocales))

"""*******************************Concatenar Cadenas*******************************"""
frase = 'Mi banda favorita es:'
complemento = 'Yes'
print(frase, complemento) # ',' agrega un espacio
print(frase + ' ' + complemento)
print("La frase era {}, y el respondio: {}".format(frase, complemento))
print(f"La frase era {frase}, y el respondio: {complemento}")

"""*******************************Booleans*******************************"""
casado = False
soltero = True
print(f"Casado? {casado} Soltero? {soltero}")

x = 10
y = 4
comparacion = x > y
print(f"{x} > {y}? {comparacion}")
y = 10
comparacion = x >= y
print(f"{x} >= {y}? {comparacion}")
x = 23
comparacion = x < y
print(f"{x} < {y}? {comparacion}")

"""*******************************Input*******************************"""
nombre = input("Cual es tu nombre? ")
print("Bienvenido",nombre)

print(input("Cual es tu edad? "))

goles1 = int(input("Cauntos goles hiciste ayer? "))
goles2 = int(input("Cauntos goles hiciste hoy? "))
print("Total de goles:", goles1 + goles2)