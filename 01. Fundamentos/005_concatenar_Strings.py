# Existen muchas manera de concatenar Strings (cadenas):

myFavoriteGroup = 'Pink floyd'
print('My favorite group is: ' + myFavoriteGroup) # Agregando un +, se unen tal cual.

myFavoriteGroup = 'Pink floyd' + ' ' + 'The best Rock Band'
print('My favorite group is: ' + myFavoriteGroup)

# More forms of print
print('My favorite group is:', myFavoriteGroup) # Agregando una ',', se agrega un espacio.
print(f'My favorite group is: {myFavoriteGroup}') # 'f' fromato de Strings para escribir las variables dentro de la cadena usando corchetes {}

num1 = '1'
num2 = '2'
print(int(num1) + int(num2)) # Transformar a int para poder sumar

# Mas ejemplos:
color_auto = "rojo"
matricula = 234
print("Mi auto es {} y de matricula {}.".format(color_auto, matricula)) # Manera antigua del format
print(f"Mi auto es {color_auto} y de matricula {matricula}.")

x = 10
y = 5
print("La suma de {} y {} es: {}.".format(x, y, x+y)) 
print(f"La suma de {x} y {y} es: {x+y}.")