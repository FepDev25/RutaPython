from tkinter import *

def mostrar_seleccion():
    resultado.config(text=f"Seleccionado: {opcion_seleccionada.get()}")

def activar_desactivar():
    estado_check = estado_checkbutton.get()
    if estado_check == 1:
        resultado.config(fg="green", text="Checkbutton activado")
    else:
        resultado.config(fg="red", text="Checkbutton desactivado")

ventana = Tk()
ventana.title("Ejemplo con más componentes")

# Etiqueta y entrada
etiqueta = Label(ventana, text="Introduce tu nombre:")
etiqueta.pack()

entrada = Entry(ventana)
entrada.pack()

# Radiobutton
opcion_seleccionada = StringVar()
opcion_seleccionada.set("Opción 1")

radiobutton1 = Radiobutton(ventana, text="Opción 1", variable=opcion_seleccionada, value="Opción 1", command=mostrar_seleccion)
radiobutton2 = Radiobutton(ventana, text="Opción 2", variable=opcion_seleccionada, value="Opción 2", command=mostrar_seleccion)

radiobutton1.pack()
radiobutton2.pack()

# Checkbutton
estado_checkbutton = IntVar()
checkbutton = Checkbutton(ventana, text="Activar/Desactivar", variable=estado_checkbutton, command=activar_desactivar)
checkbutton.pack()

# Botón
boton_mostrar = Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
boton_mostrar.pack()

# Resultado dinámico
resultado = Label(ventana, text="")
resultado.pack()

ventana.mainloop()
