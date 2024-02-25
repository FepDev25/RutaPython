# Operaciones matematicas basicas

x = 4
# x: Nombre de la variable.
# 4: Valor de la variable, conocida como "literal".

y = 6
z = x + y
print(x)
print(y)
print(z)

print(id(x)) # id(): Devuelve la pocision de memoria de una variable asignada.
print(id(y))
print(id(z))

# Mas ejemplos con contenacion de cadenas:
x = 6
y = 2
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

print(f"{7} // {2} = {7 // 2}") # "//" Hace referencia a division entera
print(f"{7} % {2} = {7 % 2}") # "%" Hace referencia a modulo o residuo

print(f"{6} elevado a la {2} = {6 ** 2}") # "**" Hace referencia potencia
print(f"La raiz cuadrada de {9} = {9 ** 0.5}")

print(2 + 3) # 5
print(3 - 2) # 1
print(3 * 2 ) # 6
print(3 / 2 ) # 1.5
print(3 ** 2 ) #9