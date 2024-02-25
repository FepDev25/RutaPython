# Este tipo de argumentos nos indican que no se tiene claro el numero de parametros que se le tiene
# que pasar a la funcion 

def listar_nombres(*nombres):  # De manera interna son una tuplade valores
    for nombre in nombres:
        print(nombre)
listar_nombres('Felipe','Diego','Mario')
listar_nombres('Felipe','Diego','Mario','Carlos','Alex')


def sumarValores(*args):
    valor = 0
    for i in args:
        valor += i
    return valor
print(sumarValores(3,1,5,6,7))
print(sumarValores(3,4,1))

def multiplicar_valores(*args):
    valor = 1
    for i in args:
        valor *= i
    return valor
print(multiplicar_valores(3,1,5,6,7))
print(multiplicar_valores(9,1,3,4,1))

# Doble asterisco para pasar argumentos de clave - valor
def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")

listarTerminos(Uno=1)
listarTerminos(Uno=1, Dos="dos ", Tres=3, Cuatro=4) # Las claves no llevan comillas


# Python realiza la funcion segun el tipo de datos que le demos como argumentos
def desplegarNombres(nombres):
    for nombre in nombres:
       print(nombre)

nombres = ['Juan', 'Karla', 'Leonel']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres([1,2])





def suma_multiple(*args):
    return sum(args)

suma = suma_multiple(3,2,1,2,3,1,3,7,8,9,12)

def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total = total + valor

    return total

def suma_total(num1, num2, *args, **kwargs):
    print(f"Primer numero {num1}")
    print(f"Segundo numero {num2}")

    suma = 0
    for i in args:
        suma += i

    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total = total + valor

    return (suma, total)

args = [6, 4, 3, 22, 13]
kwargs = {'x':3, 'y':5, 'z':10}
suma, total = suma_total(1, 4, *args,**kwargs)
print(suma)
print(total)