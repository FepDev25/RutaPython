from tkinter import Tk, Label, Entry, Button, StringVar, IntVar, Radiobutton, Checkbutton, messagebox
from tkinter.ttk import Combobox

def guardar_formulario():
    nombre = entry_nombre.get()
    genero = opcion_genero.get()
    es_cliente = es_cliente_var.get()

    if es_cliente == 1:
        es_cliente = "Si"
    else:
        es_cliente = "No"
    mensaje = f"Formulario guardado:\nNombre: {nombre}\nGénero: {genero}\n¿Cliente frecuente?: {es_cliente}"
    messagebox.showinfo("Información", mensaje)

ventana = Tk()
ventana.title("Formulario Extenso")

# Nombre
label_nombre = Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_nombre = Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

# Género
label_genero = Label(ventana, text="Género:")
label_genero.grid(row=1, column=0, padx=10, pady=5, sticky="w")

generos = ["Femenino", "Masculino", "Otro"]
opcion_genero = StringVar()
opcion_genero.set(generos[0])

for i, genero in enumerate(generos):
    radiobutton_genero = Radiobutton(ventana, text=genero, variable=opcion_genero, value=genero)
    radiobutton_genero.grid(row=1, column=i + 1, padx=10, pady=5)

# Idiomas
label_idiomas = Label(ventana, text="Idiomas:")
label_idiomas.grid(row=2, column=0, padx=10, pady=5, sticky="w")

idiomas = ["Inglés", "Español", "Francés", "Alemán"]
idiomas_seleccionados = []

for i, idioma in enumerate(idiomas):
    checkbutton_idioma = Checkbutton(ventana, text=idioma, variable=IntVar())
    checkbutton_idioma.grid(row=2, column=i + 1, padx=10, pady=5)
    idiomas_seleccionados.append(checkbutton_idioma)

# Cliente frecuente
label_cliente = Label(ventana, text="¿Es cliente frecuente?")
label_cliente.grid(row=3, column=0, padx=10, pady=5, sticky="w")

es_cliente_var = IntVar()
checkbutton_cliente = Checkbutton(ventana, variable=es_cliente_var)
checkbutton_cliente.grid(row=3, column=1, padx=10, pady=5)

# Botón de guardar
boton_guardar = Button(ventana, text="Guardar Formulario", command=guardar_formulario)
boton_guardar.grid(row=4, column=0, columnspan=3, pady=10)

# Establecer un tamaño mínimo
ventana.minsize(700, 300)

# Ajuste para centrar la ventana
ancho_ventana = 700
alto_ventana = 300

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

x_pos = int((ancho_pantalla / 2) - (ancho_ventana / 2))
y_pos = int((alto_pantalla / 2) - (alto_ventana / 2))

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

ventana.mainloop()
