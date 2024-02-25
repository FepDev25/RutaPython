import os


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    def __init__(self):
        pass

    @classmethod
    def agregar_pelicula(cls, pelicula):
        archivo = open(cls.ruta_archivo, 'a', encoding='utf8')
        archivo.write(pelicula.nombre + '\n')
        archivo.close()
        return archivo

    @classmethod
    def listar(cls):
        archivo = open(cls.ruta_archivo, 'r', encoding='utf8')
        print("Listado de Peliculas: ".center(50, '-'))
        print(archivo.read())
        archivo.close()

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
