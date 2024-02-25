from pathlib import Path
import os
from os import system

ruta = Path('/Users/karenperalta/Desktop/Recetas')

menu = """1. Leer receta.
2. Crear rectea.
3. Crear categoria.
4. Eliminar receta.
5. Eliminar categoria.
6. Finalizar Programa.
"""


def elegir_carpeta(ruta_carpetas):
    contador = 0
    lista = []
    for elemento in ruta_carpetas.glob("*"):
        if elemento.is_dir():  # Verifica si el elemento es una carpeta
            print(f"{contador + 1}. {elemento.name}")  # Imprime el nombre de la carpeta
            lista.append(elemento.stem)
            contador += 1
    eleccion = ''
    while eleccion not in lista:
        eleccion = input("Ingrese la carpeta que desea: ")
    new_ruta = Path(ruta_carpetas, eleccion)
    return new_ruta


def elegir_receta(new_ruta):
    contador = 1
    lista = []
    for txt in new_ruta.glob("**/*.txt"):
        print(f"{contador}. {txt.stem}")
        lista.append(txt.stem)
        contador += 1
    receta = ''
    while receta not in lista:
        receta = input("Ingrese la receta que desea: ")
    receta_txt = receta + ".txt"
    new_ruta_dos = Path(new_ruta, receta_txt)

    return new_ruta_dos


def leer_rectea(ruta_carpetas):
    new_ruta = Path(elegir_carpeta(ruta_carpetas))
    new_ruta_dos = Path(elegir_receta(new_ruta))
    leer = new_ruta_dos.read_text()
    print("-------------------------------")
    print(leer)
    print("-------------------------------")
    input("Presione enter para continuar.")


def crear_receta(ruta_carpetas):
    new_ruta = Path(elegir_carpeta(ruta_carpetas))
    nombre = crear_nombre()
    nombre_txt = nombre + ".txt"
    contenido = crear_contenido()

    os.chdir(new_ruta)

    archi1 = open(nombre_txt, 'w')
    archi1.write(contenido)

    os.getcwd()


def eliminar_receta(ruta_carpetas):
    new_ruta = Path(elegir_carpeta(ruta_carpetas))
    new_ruta_dos = Path(elegir_receta(new_ruta))
    os.remove(new_ruta_dos)
    print("-------------------------------")
    print("Receta eliminada exitosamente")
    print("-------------------------------")
    input("Presione enter para continuar.")


def eliminar_categoria(ruta_carpetas):
    new_ruta = Path(elegir_carpeta(ruta_carpetas))
    os.rmdir(new_ruta)
    print("-------------------------------")
    print("Categoria eliminada exitosamente")
    print("-------------------------------")
    input("Presione enter para continuar.")


def crear_nombre():
    nombre = input("Ingrese el nombre de su receta: ")
    return nombre


def crear_contenido():
    contenido = input("Ingrese el contenido de su receta: ")
    return contenido


def crear_categoria(ruta_carpetas):
    categoria = input("Ingrese el nombre de la nueva categoria: ")
    new_ruta = Path(ruta_carpetas, categoria)
    new_ruta.mkdir(parents=True)


def menu_rectas():
    opcion = 0
    while opcion != 6:
        print(menu)
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case '1':
                leer_rectea(ruta)
                system('clear')
            case '2':
                crear_receta(ruta)
                system('clear')
            case '3':
                crear_categoria(ruta)
                system('clear')
            case '4':
                eliminar_receta(ruta)
                system('clear')
            case '5':
                eliminar_categoria(ruta)
                system('clear')
            case '6':
                break


menu_rectas()
