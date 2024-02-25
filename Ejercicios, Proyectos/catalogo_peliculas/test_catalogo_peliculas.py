from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula


menu = """1. Agregar
2. Listar
3. Eliminar
4. Salir
"""


def agregar_pelicula():
    nombre = input("Ingrese el nombre de la pelicula: ")
    pelicula = Pelicula(nombre)
    return pelicula


def inicio():
    opcion = 0
    while opcion != 4:
        print(menu)
        try:
            opcion = int(input("Ingrese la opcion: "))
        except Exception as e:
            print(f"Ocurrio un error: {e}")
            opcion = 0
        match opcion:
            case 1:
                pelicula_aux = agregar_pelicula()
                CatalogoPeliculas.agregar_pelicula(pelicula_aux)
            case 2:
                CatalogoPeliculas.listar()
            case 3:
                CatalogoPeliculas.eliminar()


inicio()
