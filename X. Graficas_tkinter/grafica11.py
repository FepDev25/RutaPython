import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import PhotoImage
import os

class VentanaImagenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Resolucion de la Ecuacion")

        # Lista de rutas de imágenes
        self.rutas_imagenes = ["primero.png", "segundo.png", "tercero.png"]

        # Inicializar la imagen actual
        self.indice_imagen_actual = 0
        self.imagen_actual = self.cargar_imagen(self.rutas_imagenes[self.indice_imagen_actual])

        # Mostrar la imagen en un widget Label
        self.label_imagen = tk.Label(root, image=self.imagen_actual)
        self.label_imagen.pack(pady=10)

        # Botón para cambiar a la siguiente imagen
        self.boton_siguiente = tk.Button(root, text="Siguiente Imagen", command=self.mostrar_siguiente_imagen)
        self.boton_siguiente.pack(pady=10)

    def cargar_imagen(self, ruta):
        imagen_pillow = Image.open(ruta)
        imagen_tk = ImageTk.PhotoImage(imagen_pillow)
        return imagen_tk

    def mostrar_siguiente_imagen(self):
        # Incrementar el índice de la imagen actual
        self.indice_imagen_actual = (self.indice_imagen_actual + 1) % len(self.rutas_imagenes)

        # Cargar la siguiente imagen
        nueva_imagen = self.cargar_imagen(self.rutas_imagenes[self.indice_imagen_actual])

        # Actualizar la imagen en el widget Label
        self.label_imagen.configure(image=nueva_imagen)
        self.label_imagen.image = nueva_imagen  # Mantener una referencia

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaImagenes(root)
    root.mainloop()
