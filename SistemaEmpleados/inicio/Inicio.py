import sys
sys.path.append('/Users/karenperalta/Desktop/estudios/Python/SistemaEmpleados')
from control.Controlador import *

def menu():
    opcion=0
    control = Control("empleados.txt", "vista(aun no)")
    control.cargar_empleados()
    menuTexto = """
******* Sistema de Empleados *******
1. Agregar Empleado
2. Eliminar Empleado
3. Editar Empleado
4. Listar Empleados
5. Aumentar Sueldo
6. Salir
Seleccione una opcion:
"""
    while opcion!="6":
        print(menuTexto)
        opcion = input()
        match opcion:
            case "1":
                nombre = input("Ingrese nombre: ")
                edad = input("Ingrese edad: ")
                cedula = input("Ingrese cedula: ")
                salario = input("Ingrese salario: ")
                cargo = input("Ingrese cargo: ")
                aux = Empleado(nombre, edad, cedula, salario, cargo)
                control.agregar_empleado(aux)
            case "2":
                listaEmpleados = control._empleados
                for pos, empleado in enumerate(listaEmpleados):
                    print(f"{pos}. {empleado}")
                indiceEmpleado = input("Seleccione el empleado a eliminar: ")
                control.eliminar_empleado(control._empleados[int(indiceEmpleado)])
            case "3":
                listaEmpleados = control._empleados
                for pos, empleado in enumerate(listaEmpleados):
                    print(f"{pos}. {empleado}")
                indiceEmpleado = input("Seleccione el empleado a editar: ")
                empleado_editable = control.obtener_por_cedula(control._empleados[int(indiceEmpleado)])
                cedula_empleado = empleado_editable._cedula
                nombre = input("Ingrese nombre: ")
                edad = input("Ingrese edad: ")
                salario = input("Ingrese salario: ")
                cargo = input("Ingrese cargo: ")
                aux = Empleado(nombre, edad, cedula_empleado, salario, cargo)
                control.editar_empleado(aux)
            case "4":
                control.listar_empleados()
            case "5":
                listaEmpleados = control._empleados
                for pos, empleado in enumerate(listaEmpleados):
                    print(f"{pos}. {empleado}")
                indiceEmpleado = input("Seleccione el empleado al que se le aumentara el sueldo: ")
                empleado_editable = control.obtener_por_cedula(control._empleados[int(indiceEmpleado)])
                cedula = empleado_editable._cedula
                nombre = empleado_editable._nombre
                edad = empleado_editable._edad
                salario = input("Ingrese nuevo salario: ")
                cargo = empleado_editable._cargo
                aux = Empleado(nombre, edad, cedula, salario, cargo)
                control.editar_empleado(aux)
            case _:
                print("Opcion incorrecta")

menu()