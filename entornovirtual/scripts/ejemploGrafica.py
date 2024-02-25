import tkinter as tk


# Función que se ejecuta al hacer clic en el botón
def on_button_click():
    label.config(text="Hola, " + entry.get())


# Crear una ventana principal
root = tk.Tk()
root.title("Ejemplo Tkinter")

# Crear un widget Label
label = tk.Label(root, text="Ingrese su nombre:")

# Crear un widget Entry para obtener la entrada del usuario
entry = tk.Entry(root)

# Crear un botón que ejecuta la función on_button_click al hacer clic
button = tk.Button(root, text="Saludar", command=on_button_click)

# Colocar los widgets en la ventana
label.pack()
entry.pack()
button.pack()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
