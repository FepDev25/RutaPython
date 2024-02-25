# Condicionales: 

condicion = True

if condicion:
    print('Condicion verdadera')
elif not condicion:
    print('Condicion falsa')
else:
    print('Condicion falsa')


if 10 > 9:
    print("10 es mayor que 9")

if 5 == 9:
    print("Son iguales")
else:
    print("Incorrecto")

mascota = "gato"
if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("No se que animal tienes")

# El valor verdadero es un valor diferente de vacio
if 10:
    print("Diferente de vacio")
# El valor falso es un valor vacio
if not '':
    print("Vacio")