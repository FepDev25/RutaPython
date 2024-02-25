print("Proporcione los siguientes datos del libro: ")
nombre = input("Ingrese el nombre del libro: ")
id = int(input('Ingrese el id del libro: '))
precio = float(input("Ingrese el precio del libro: "))
envioG = input('Indica si es envio gratuito (True / False): ')
if envioG == 'True':
    envioG = True
elif envioG == 'False':
    envioG = False
else:
    envioG = 'Valor incorrecto, debe escribir True o False.'

print(f'''
Nombre del libro: {nombre}
Id del libro: {id}
Precio del libro: {precio}
Envio gratuito: {envioG}
''')