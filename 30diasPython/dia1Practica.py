"""
Ejercicio: Nivel 1
Compruebe la versión de Python que está utilizando
Abra el shell interactivo de python y realice las siguientes operaciones. Los operandos son 3 y 4.
suma (+)
sustracción(-)
multiplicación(*)
módulo(%)
división(/)
exponencial(**)
operador de división de piso(//)
Escriba cadenas en el shell interactivo de python. Las cadenas son las siguientes:
Su nombre
tu apellido
Tu país
Estoy disfrutando de 30 días de python
Compruebe los tipos de datos de los siguientes datos:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finlandia']
Su nombre
tu apellido
Tu país
Ejercicio: Nivel 2
Cree una carpeta llamada day_1 dentro de la carpeta 30DaysOfPython. Dentro de la carpeta day_1, cree un archivo python helloworld.py y repita las preguntas 1, 2, 3 y 4. Recuerde usar print() cuando esté trabajando en un archivo python. Navegue hasta el directorio donde ha guardado su archivo y ejecútelo.
Ejercicio: Nivel 3
Escriba un ejemplo para diferentes tipos de datos de Python, como número (entero, flotante, complejo), cadena, booleano, lista, tupla, conjunto y diccionario.
Encuentra una distancia euclidiana entre (2, 3) y (10, 8)
"""

# Ejercicio 1
#Version de python: Python 3.9.13
print(10 + 11)
print(4 - 6)
print(3 * 14)
print(17 % 2)
print(225 / 25)
print(4 ** 5)
print(9 // 2)
nombre = "Felipe"
apellido = "Peralta"
pais = "Ecuador"
print("Estoy disfrutando aprender :)")
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
9.8
3.14
4 - 4j
print(type(['Asabeneh', 'Python', 'Finlandia']))
print(type(nombre))
print(type(apellido))
print(type(pais))

# Nivel 3
int_1 = 5
float_1 = 3.14
complejo_1 = 6 + 7j
string_1 = "Hola"
boolean_1 = True
lista_1 = [1,2,3,4,5]
tupla_1 = (1,2,3)
set_1 = {4,10,12,1,19}
dict_1 = {"Nombre": "Felipe", "Apellido": "Peralta"}

distancia_x = 2 - 10
distancia_y = 3 - 8
distancia = ((distancia_x ** 2) + (distancia_y ** 2))**0.5
print(f"Distancia euclidiana entre (2, 3) y (10, 8): {distancia} ")