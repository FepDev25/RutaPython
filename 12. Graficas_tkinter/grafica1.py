from tkinter import *

# Raiz
raiz = Tk()

etiqueta = Label(raiz, text="Hola, mundo!")
etiqueta.pack()

# Ejecutar el bucle infinitio
# Va a estar escuchando los eventos permanentemente hasta finalizar el programa
raiz.mainloop() # Siempre va al final