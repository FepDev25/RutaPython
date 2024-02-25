"""
Declara tu edad como variable entera
Declara tu altura como una variable flotante
Declarar una variable que almacene un número complejo
"""
edad = 18
altura = 1.73
complex = 4 + 3j
print(f" {type(edad)} {type(altura)} {type(complex)} ")

"""
Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo 
(área = 0,5 xbxh).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))
print(f"El area del triangulo es: {0.5 * base * altura}")
"""

"""
Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo
 (perímetro = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
ladoA = int(input("Ingrese el primer lado del triangulo: "))
ladoB = int(input("Ingrese el segundo lado del triangulo: "))
ladoC = int(input("Ingrese el tercer lado del triangulo: "))
print(f"El perimetro del triangulo es: {ladoA + ladoB + ladoC}")
"""

"""
Obtenga la longitud y el ancho de un rectángulo usando el indicador. Calcula su área (área = largo x ancho) 
y perímetro (perímetro = 2 x (largo + ancho))
base = int(input("Ingrese la base del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))
print(f"El area del rectángulo es: {base * altura}")
print(f"El perimetro del rectángulo es: {2 * (base + altura)}")
"""

"""
Obtenga el radio de un círculo usando el indicador. Calcula el área (área = pi xrxr) y la circunferencia (c = 2 x pi xr) donde pi = 3,14.
radio = float(input("Ingrese el radio del circulo: "))
print(f"El area del circulo es {3.14 * radio * radio} ")
print(f"La circunferencia de circulo es {2 * 3.14 * radio} ")
"""

"""
Calcule la pendiente, la intersección x y la intersección y de y = 2x -2
"""
pendiente1 = 2
corte_x = 2 / 2
corte_y = -2


"""
La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10)
"""
pendiente2 = int((2 - 10) / (2 - 6))
print(pendiente2)
distanciaE = (((6-2)**2) + ((10 - 2)**2))** 0.5
print(distanciaE)

"""
Compara las pendientes en las tareas 8 y 9.
"""
iguales = pendiente1 == pendiente2
print(iguales)


"""
Calcula el valor de y (y = x^2 + 6x + 9). Trate de usar diferentes valores de x y descubra en qué valor de x y será 0.
"""
y = (-3)**2 + 6*-3 + 9
print(y)


"""
Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación falsa.
"""
pythonLen = len("python")
dragonLen = len("dragon")
print(f"{pythonLen} {dragonLen}")
print(pythonLen != dragonLen)


"""
Use un operador para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
"""
print(('on' in 'python') and ('on' in 'dragon'))


"""
Espero que este curso no esté lleno de jerga . Use el operador in para verificar si hay jerga en la oración.
"""
print('jerga' in 'Espero que este curso no esté lleno de jerga.')


"""
No hay 'on' tanto en dragon como en python
"""
print(('on' not in 'dragon') and ('on' not in 'python'))


"""
Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
"""
longitud = len("python")
longitud = float(longitud)
print(longitud)
longitud = str(longitud)
print(longitud)



""""
Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?
numero = int(input("Ingrese un numero: "))
if (numero % 2 == 0):
    print("El numero es par")
else: print("El numero es impar")
"""

""""
Verifique si la división del piso de 7 por 3 es igual al valor int convertido de 2.7.
"""
print((7/3) == 2.7)


"""
Compruebe si el tipo de '10' es igual al tipo de 10
"""
print(type('10') == type(10))

"""
Comprueba si int('9.8') es igual a 10
"""
print(type(int(9.8)) == type(10))


"""
Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rate} ")
"""


"""
Escriba un script que solicite al usuario que ingrese el número de años. Calcular el número de segundos que puede vivir una persona.
 Supongamos que una persona puede vivir cien años.
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {years * 31536000}")
"""


"""
Escriba un script de Python que muestre la siguiente tabla
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
for i in range(1,6):
    print(f" {i} 1 {i} {i**2} {i**3} ")

