from tkinter import *

def agregar_elemento():
    elemento = entrada.get()
    cuadro_lista.insert("end", elemento)

ventana = Tk()

cuadro_lista = Listbox(ventana)
cuadro_lista.pack()

entrada = Entry(ventana)
entrada.pack()

boton_agregar = Button(ventana, text="Agregar elemento", command=agregar_elemento)
boton_agregar.pack()

ventana.mainloop()
