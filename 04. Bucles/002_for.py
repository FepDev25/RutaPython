# Ciclo for, incluye contador en su compocision

for i in "Hola":
    print(i)

for i in range(0,10): # Imprimir numero indicando un rango
    print(i)

for letra in "Holanda":
    if letra == "a":
        print(f"letra encontrada: {letra}")
        break # Break utilizado para romper el bucle
    print(letra)

for i in range(0,6):
    if i % 2 != 0:
        continue # Continue utilizado para romper la iteracion y avanzar a la siguiente
    print(i)

nombres = ["Juan", "Ana", "Lulu", "Fran"]
for elemento in nombres: # Iterar listas
    print(f"Hola {elemento}")

for i in "Hola Bruno": # Iterar cadenas
    print(i)

numeros = [1,2,3,4,5]
mi_valor = 0
for i in numeros:
    mi_valor = mi_valor + i
    print(mi_valor)

nombres = ["Felipe", "Diego", "Maria"]
for i in nombres:
    print(f"Nombre {nombres.index(i)}: {i}")

for a,b in [[1, 2], [3, 4], [5, 6]]: # Dos variables iniciales que almacenan los dos valores de cada pasada
    print(a)
    print(b)

dic = {'c1': 'a', 'c2': 'b', 'c3': 'c'}
for i in dic: # Imprime: c1, c2, c3
    print(i)

for i in dic.items(): # Imprime ('c1', 'a') ('c2', 'b') ('c3', 'c')
    print(i)

for i in dic.values(): # Imprime: a, b, c
    print(i)

print('Uso de break: ')
nombre = 'Felipe'
for i in nombre:
    if i == 'l':
        break
    print(i)

print('Uso de continue: ')
nombre = 'Felipe'
for i in nombre:
    if i == 'l':
        continue
    print(i)
