import sys
sys.path.append('/Users/karenperalta/Desktop/estudios/Python/SistemaEmpleados')
from modelo.modelos import *
from manipulacion_archivos.archivos import *
import re

class Control:
    def __init__(self, nombreArchivo, vista):
        self._nombreArchivo = nombreArchivo
        self._vista = vista
        self._empleados = []
        self._manejoArchivos = ManejoArchivos(self._nombreArchivo)

    @property
    def empleados(self):
        return self._empleados
    
    @property
    def manejoArchivos(self):
        return self._manejoArchivos

    def cargar_empleados(self):
        self._empleados = self.manejoArchivos.cargar_empleados()

        
    def guardar_empleados_en_archivo(self):
        self.manejoArchivos.guardar_empleados_en_archivo(self._empleados)

    def guardar_nuevo_empleado_en_archivo(self, empleado):
        self.manejoArchivos.guardar_nuevo_empleado_en_archivo(empleado)
    
    def agregar_empleado(self, empleado):
        if (self.validar_cedula(empleado.cedula) and self.validar_repetidos(empleado.cedula)):
            self.empleados.append(empleado)
            self.guardar_nuevo_empleado_en_archivo(empleado)
            print("Empleado agregado/editado Correctamente")
    
    def editar_empleado(self, empleado):
        try:
            self.eliminar_empleado(empleado)
            self.agregar_empleado(empleado)
        except Exception as e:
            print("Error al editar")
        else:
            print("Empleado editado")


    def eliminar_empleado(self, empleado):
        try:
            self.empleados.remove(self.obtener_por_cedula(empleado))
            self.guardar_empleados_en_archivo()
            print("Empleado eliminado")
        except Exception as e:
            print("Error al eliminar")

    def obtener_por_cedula(self, empleado):
        for i in self.empleados:
            if i.cedula == empleado.cedula:
                return i
        return None

    
    def listar_empleados(self):
        for empleado in self.empleados:
            print(empleado)

    def validar_cedula(self, cedula):
        patron_cedula = r"^0\d{9}$"
        if re.match(patron_cedula, cedula):
            return True
        else:
            print("Cedula Invalida")
            return False

    def validar_repetidos(self, cedula):
        for i in self.empleados:
            if (i.cedula == cedula):
                print("Cedula Repetida")
                return False
        return True