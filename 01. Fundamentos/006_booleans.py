# Type Boolean: Este tipo de datos solo puede almacenar dos valores: True y False
# Se usa especialmente en condicionales o para comprobar algunas operaciones.

miBoolean1 = True # Definiciones de Booleanos
miBoolean2 = False
print(miBoolean1, miBoolean2)

miBoolean3 = 3 > 1 # True
miBoolean4 = 1 > 2 # False
print(miBoolean3, miBoolean4)
miBool3 = 5 > 3
miBool4 = 5 > 7

if miBoolean1: # Aqui la ejecucion entrara en el if en caso de que miBoolean1 sea verdadera
    print('True')
else:
    print('False')


lista = [1, 2, 3]
miBool5 = 2 in lista # Pregunta si 2 esta dentro de la lista
miBool6 = 7 not in lista # Pregunta si 7 no esta dentro de la lista

print(miBool3, miBool4, miBool5, miBool6)

lista_de_bools = [miBool3, miBool4, miBool5, miBool6] # Lista de booleanos

for i in lista_de_bools: # Imprimir tipo de datos booleanos
    print(type(i))
