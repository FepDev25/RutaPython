# Ciclo while
# Se debe incluir contador propio, puede generarse infinitos.

condicion = True

while(condicion == True):
    print("Hola mundo")
    condicion = False

c = 0
while(c <= 5):
    print(c)
    c += 1

c = 5
while(c >= 1):
    print(c)
    c -= 1

# Opcionalmente se puede utilizar un else para indicar que se termino el bucle
c = 0
while c <= 10:
    print(c)
    c+=1
else:
    print("El bucle ha finalizado")
