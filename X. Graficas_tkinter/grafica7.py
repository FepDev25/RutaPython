from tkinter import *

def mostrar_valor_deslizador(valor):
    mensaje_deslizador.config(text=f"Valor seleccionado: {valor}")

def mostrar_valor_spinbox():
    valor_spinbox = spinbox.get()
    mensaje_spinbox.config(text=f"Valor seleccionado: {valor_spinbox}")

def mostrar_seleccion():
    resultado.config(text=f"Hola {entrada.get()}, eres un {opcion_seleccionada.get()} y tienes {deslizador.get()} de fuerza")

ventana = Tk()
ventana.title("Ejemplo con más componentes")

# Etiqueta y entrada
etiqueta = Label(ventana, text="Introduce tu nombre:")
etiqueta.pack()

entrada = Entry(ventana)
entrada.pack()

# Radiobutton
opcion_seleccionada = StringVar()
opcion_seleccionada.set("Humano")

radiobutton1 = Radiobutton(ventana, text="Humano", variable=opcion_seleccionada, value="Humano")
radiobutton2 = Radiobutton(ventana, text="Animal", variable=opcion_seleccionada, value="Animal")

radiobutton1.pack()
radiobutton2.pack()

# Checkbutton
estado_checkbutton = IntVar()
checkbutton = Checkbutton(ventana, text="Si/No", variable=estado_checkbutton)
checkbutton.pack()

# Botón
boton_mostrar = Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
boton_mostrar.pack()

# Deslizador (Scale)
deslizador = Scale(ventana, from_=0, to=100, orient="horizontal", command=mostrar_valor_deslizador)
deslizador.pack()

mensaje_deslizador = Message(ventana, text="", width=200)
mensaje_deslizador.pack()

# Spinbox
spinbox = Spinbox(ventana, from_=0, to=10, command=mostrar_valor_spinbox)
spinbox.pack()

mensaje_spinbox = Message(ventana, text="", width=200)
mensaje_spinbox.pack()

# Resultado dinámico
resultado = Label(ventana, text="")
resultado.pack()

ventana.mainloop()
