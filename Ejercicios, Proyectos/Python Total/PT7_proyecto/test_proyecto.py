from Cliente import Cliente
from os import system


def crear_cliente():
    print("*********INGRESO CLIENTES*********")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    balance = int(input("Ingrese balance inicial: "))

    cliente = Cliente(nombre, apellido, balance)
    print("Cliente ingresado con exito.")
    return cliente


def seleccionar_cliente(lista_clientes):
    contador = 1
    for cliente in lista_clientes:
        print(f"{contador}. {cliente.nombre}")
        contador += 1
    seleccion = int(input("Seleccione cliente: "))
    seleccion -= 1
    return lista_clientes[seleccion]


def depositar(cliente):
    valor = float(input("Ingrese el valor que va a depositar: "))
    cliente.depositar(valor)
    print(cliente)


def retirar(cliente):
    valor = float(input("Ingrese el valor que va a retirar: "))
    cliente.retirar(valor)
    print(cliente)


def enter_continuar():
    input("Presione enter pata continuar.")
    system('clear')


def ver_todos(lista_clientes):
    for cliente in lista_clientes:
        print(cliente)


menu = """1. Ingresar
2. Ver datos
3. Depositar
4. Retirar
5. Ver todos
6. Salir
"""


def inicio():
    opcion = 0
    clientes = []
    while opcion != 6:
        print(menu)
        opcion = int(input("Ingrese la opcion que desea: "))
        match opcion:
            case 1:
                cliente = crear_cliente()
                clientes.append(cliente)
                enter_continuar()
            case 2:
                cliente_aux = seleccionar_cliente(clientes)
                print(cliente_aux)
                enter_continuar()
            case 3:
                cliente_aux = seleccionar_cliente(clientes)
                depositar(cliente_aux)
                enter_continuar()
            case 4:
                cliente_aux = seleccionar_cliente(clientes)
                retirar(cliente_aux)
                enter_continuar()
            case 5:
                ver_todos(clientes)
                enter_continuar()


inicio()
