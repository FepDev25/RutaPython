# Funciones: Bloques de codigo que nos permite ejecutar una secuencia de codigo n cantidad de veces
# Ayuda a no sobreescribir codigo

def mi_funcion(nombre): # Definicion de una funcion
    print(f"Saludos {nombre}")

mi_funcion('Maria') # "Llamada a la funcion"
mi_funcion('Diego')
mi_funcion('Pepe')

def sumar(x,y):
    return x + y

suma = sumar(8,9)
print(suma)

# Asignar valores por default a las variables locales
def sumar_con_default(x = 0, y = 0):
    return x + y

print(sumar_con_default()) # 0
print(sumar_con_default(7)) # 7
print(sumar_con_default(2,9)) # 11

def sumar_indicado(y = 0, x = 0) -> int: # Dar una pista del tipo de dato que rotorna la funcion
    return x + y

print(sumar_indicado())
print(sumar_indicado(7))
print(sumar_indicado(2,9))

def calcular_pago_total(sin_impuestos, impuesto):
    return sin_impuestos + (sin_impuestos * impuesto/100)


sin_impuestos = int(input("Ingrese el pagosin impuestos: "))
impuesto = int(input("Ingrese el porcentaje del impuesto: "))

print(f"Pago con impuestos: {calcular_pago_total(sin_impuestos, impuesto)}")

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
    return (cafe_mas_caro, precio_mayor)

precios_cafe = [('capuchino', 1.5),('expresso', 1.2), ('moka',1.9)]

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} y cuesta ${precio}")

def chequear_3_cifras(lista):
    respuesta = []
    for i in lista:
        if i in range(100,1000):
            respuesta.append(i)
    return respuesta

def comprobar_3_cifras(lista):
    for i in lista:
        if i in range(100,1000):
            return True
    return False



print()
resultado1 = chequear_3_cifras([545, 23, 567, 123, 12, 1000, 999])
print(resultado1)

resultado2 = comprobar_3_cifras([545, 23, 567, 123, 12, 1000, 999])
print(resultado2)