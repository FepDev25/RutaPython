# Los operadores logicos se componen de 'y' y 'o'

# Tienen los mismos valores que en las tabalas de verdad
# and: Para ser true necesita dos valores de verdad
# or: Para ser true necesita solo un valor de verdad
# not: Valor contrario

a = True
b = True
resultado = a and b
print(resultado)

a = True
b = False
resultado = a and b
print(resultado)

a = True
b = True
resultado = a or b
print(resultado)

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = 4 < 5 or 5 == 2+3
print(mi_bool)

miBool = False
if not mi_bool:
    print("A")
else:
    print("B")

# Simplificar sintaxis:
valor = 20 >= 10 and 20 <= 30
print(valor)
valor = 10 <= 20 <= 30
print(valor)
