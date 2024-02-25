numero = int(input('Ingrese un numero del 1 al 3: '))
numeroTexto = ''
if numero == 1:
    numeroTexto = 'Uno'
elif numero == 2:
    numeroTexto = 'Dos'
elif numero == 3:
    numeroTexto = 'Tres'
else:
    numeroTexto = "Valor fuera de rango."

print(f'Numero proporcionado {numero}: {numeroTexto}')
