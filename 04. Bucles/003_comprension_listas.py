lista = [i for i in 'python']
print(lista)

lista = [n for n in range(0,7)]
print(lista)

lista = [n/2 for n in range(0,22, 3)]
print(lista)

lista = [n for n in range(0,101) if n % 2 == 0]
print(lista)

lista = [n if n % 2 == 0 else 'no' for n in range(0,7)]
print(lista)

pies = [10, 20, 30, 55, 34]
metros = [round(n/3.281, 2) for n in pies]
print(metros)

