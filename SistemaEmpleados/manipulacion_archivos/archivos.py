import sys
sys.path.append('/Users/karenperalta/Desktop/estudios/Python/SistemaEmpleados')
import logging
from modelo.modelos import Empleado

class ManejoArchivos:
    def __init__(self, nombre_archivo):
        self._nombre_archivo = nombre_archivo

    def cargar_empleados(self):
        empleados_lista = []
        try:
            ruta = f'/Users/karenperalta/Desktop/estudios/Python/SistemaEmpleados/{self._nombre_archivo}'
            with open(ruta, 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    separador = linea.strip().split(',')
                    if len(separador) == 5:
                        empleado = Empleado(separador[0], separador[1], separador[2], separador[3], separador[4])
                        empleados_lista.append(empleado)
                    else:
                        logging.warning(f"Línea ignorada en carga de empleados: {linea}")
        except FileNotFoundError:
            logging.warning(f"El archivo {self._nombre_archivo} no existe. Se creará uno nuevo.")
        except Exception as e:
            logging.error(f"Error al cargar empleados: {e}")
        return empleados_lista

    def guardar_empleados_en_archivo(self, lista_empleados):
        try:
            ruta = f'/Users/karenperalta/Desktop/estudios/Python/SistemaEmpleados/{self._nombre_archivo}'
            with open(ruta, 'w') as archivo:
                for empleado in lista_empleados:
                    empleado_string = f"{empleado.nombre},{empleado.edad},{empleado.cedula},{empleado.salario},{empleado.cargo}\n"
                    archivo.write(empleado_string)
        except FileNotFoundError:
            logging.warning(f"El archivo {self._nombre_archivo} no existe. Se creará uno nuevo.")
        except Exception as e:
            logging.error(f"Error al guardar empleados en archivo: {e}")

    def guardar_nuevo_empleado_en_archivo(self, empleado):
        try:
            ruta = f'/Users/karenperalta/Desktop/estudios/Python/SistemaEmpleados/{self._nombre_archivo}'
            with open(ruta, 'a') as archivo:
                empleado_string = f"{empleado._nombre},{empleado._edad},{empleado._cedula},{empleado._salario},{empleado._cargo}\n"
                archivo.write(empleado_string)
        except FileNotFoundError:
            logging.warning(f"El archivo {self._nombre_archivo} no existe. Se creará uno nuevo.")
        except Exception as e:
            logging.error(f"Error al guardar nuevo empleado en archivo: {e}")
