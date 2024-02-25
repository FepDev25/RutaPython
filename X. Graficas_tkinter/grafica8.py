from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter.ttk import Combobox

def guardar_cliente():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    equipo = combobox.get()

    # Puedes procesar y almacenar los datos como desees, aquí solo mostramos un mensaje
    mensaje = f"Cliente guardado:\nNombre: {nombre}\nApellido: {apellido}\nTeléfono: {telefono}\nEquipo: {equipo}"
    messagebox.showinfo("Información", mensaje)

# Crear la ventana
ventana = Tk()
ventana.title("Formulario de Cliente")

# Crear etiquetas y cuadros de entrada
label_nombre = Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_nombre = Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_apellido = Label(ventana, text="Apellido:")
label_apellido.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_apellido = Entry(ventana)
entry_apellido.grid(row=1, column=1, padx=10, pady=5)

label_telefono = Label(ventana, text="Teléfono:")
label_telefono.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_telefono = Entry(ventana)
entry_telefono.grid(row=2, column=1, padx=10, pady=5)

label_equipo = Label(ventana, text="Equipo:")
label_equipo.grid(row=3, column=0, padx=10, pady=5, sticky="w")

opciones = ["Chelsea FC", "Real Madrid", "Barceleches"]
combobox = Combobox(ventana, values=opciones)
combobox.grid(row=3, column=1, padx=10, pady=5)

# Botón para guardar
boton_guardar = Button(ventana, text="Guardar Cliente", command=guardar_cliente)
boton_guardar.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
ventana.mainloop()
