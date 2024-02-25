"""
Ejercicios: Nivel 1
Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta crea un archivo llamado variables.py
Escriba un comentario de python que diga 'Día 2: 30 días de programación en python'
Declarar una variable de nombre y asignarle un valor
Declarar una variable de apellido y asignarle un valor
Declarar una variable de nombre completo y asignarle un valor
Declarar una variable de país y asignarle un valor
Declarar una variable de ciudad y asignarle un valor
Declarar una variable de edad y asignarle un valor
Declarar una variable de año y asignarle un valor
Declarar una variable is_married y asignarle un valor
Declarar una variable is_true y asignarle un valor
Declarar una variable is_light_on y asignarle un valor
Declarar múltiples variables en una línea
"""
nombre = "Felipe"
apellido = "Peralta"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
pais = "Ecuador"
ciudad = "Cuenca"
edad = 18
year = 2023
is_married = False
is_true = False
is_light_on = True
equipoLatam, equipoEuropa = "Deportivo Cuenca", "Chelsea FC"

"""
Ejercicios: Nivel 2
Verifique el tipo de datos de todas sus variables usando la función incorporada type ()
Usando la función incorporada len() , encuentre la longitud de su nombre
Compare la longitud de su nombre y su apellido
Declarar 5 como num_one y 4 como num_two
Agregue num_one y num_two y asigne el valor a un total variable
Reste num_two de num_one y asigne el valor a una variable diff
Multiplique num_two y num_one y asigne el valor a un producto variable
Divide num_one por num_two y asigna el valor a una división variable
Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
"""
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(nombre))

print(f"len nombre: {len(nombre)}, len apellido: {len(apellido)} ")

num_one = 5
num_two = 4

sum = num_one + num_two
rest = num_two - num_one
mult = num_two * num_one
div = num_one / num_two
modulo = num_two % num_one
exp = num_one ** num_two
div_p = num_one // num_two

""""
El radio de un círculo es de 30 metros.
Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
Tome el radio como entrada del usuario y calcule el área.
Use la función de entrada incorporada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras reservadas o las palabras clave de Python
"""
area = 3.141592 * (30**2)
print(area)

circunferencia = 3.141592 * (30*2)
print(circunferencia)

radio = int(input("Ingrese el radio: "))
area = 3.141592 * (radio**2)
print(f"El area del circulo con radio {radio} es {area}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
país = input("Ingrese su pais: ")
edad = int(input("Ingrese su edad: "))

help("keywords")