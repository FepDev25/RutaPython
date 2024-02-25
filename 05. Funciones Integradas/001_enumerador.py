lista = ['a', 'b', 'c']
for item in enumerate(lista):
    print(item)

for item in enumerate(range(10,16)):
    print(item)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for a, b in enumerate(lista_nombres):
    print(f'{b} se encuentra en el índice {a}')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for a,b in enumerate(lista_nombres):
    if b.startswith('M'):
        print(a)