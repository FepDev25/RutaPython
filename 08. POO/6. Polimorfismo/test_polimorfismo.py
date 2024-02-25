from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Felipe", 400)
imprimir_detalles(empleado)

gerente = Gerente("Diego", 600, "Sistemas")
imprimir_detalles(gerente)
