import tkinter as tk
from tkinter import Label, Entry, Button, Radiobutton, StringVar, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class LeyEnfriamientoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ley de Enfriamiento de Newton")

        # Etiqueta de texto como título
        title_label = Label(root, text="Ley de Enfriamiento de Newton", font=("Helvetica", 16))
        title_label.grid(row=0, column=1, pady=10)

        # Etiqueta y entrada para la temperatura ambiente
        ambient_temp_label = Label(root, text="Temperatura Ambiente:")
        ambient_temp_label.grid(row=1, column=0, padx=10, pady=5)
        self.ambient_temp_entry = Entry(root)
        self.ambient_temp_entry.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y entrada para la condición inicial 1 (t=0)
        initial_condition_1_label = Label(root, text="Condición Inicial 1 (T en t=0):")
        initial_condition_1_label.grid(row=2, column=0, padx=10, pady=5)
        self.initial_condition_1_entry = Entry(root)
        self.initial_condition_1_entry.grid(row=2, column=1, padx=10, pady=5)

        # Etiqueta y entradas para la condición inicial 2 (otro punto de tiempo)
        initial_condition_2_label = Label(root, text="Condición Inicial 2 (T y tiempo):")
        initial_condition_2_label.grid(row=3, column=0, padx=10, pady=5)
        self.initial_condition_2_temp_entry = Entry(root, width=10)
        self.initial_condition_2_temp_entry.grid(row=3, column=1, padx=5, pady=5)
        self.initial_condition_2_time_entry = Entry(root, width=10)
        self.initial_condition_2_time_entry.grid(row=3, column=2, padx=5, pady=5)

        # Radio button para seleccionar la incógnita
        self.var = StringVar()
        self.var.set("T")
        radio_label = Label(root, text="Seleccione la incógnita:")
        radio_label.grid(row=4, column=0, padx=10, pady=5)
        t_radio = Radiobutton(root, text="t  (tiempo)", variable=self.var, value="t", command=self.controlarIncognita)
        t_radio.grid(row=4, column=1, pady=5)
        T_radio = Radiobutton(root, text="T (temperatura)", variable=self.var, value="T", command=self.controlarIncognita)
        T_radio.grid(row=4, column=2, pady=5)

        # Etiqueta y entrada para la incognita
        ambient_temp_label = Label(root, text="Valor de la incognita:")
        ambient_temp_label.grid(row=5, column=0, padx=10, pady=5)
        self.ambient_temp_entry = Entry(root)
        self.ambient_temp_entry.grid(row=5, column=1, padx=10, pady=5)

        # Botón para mostrar la gráfica
        plot_button = Button(root, text="Mostrar Gráfica", command=self.plot_graph)
        plot_button.grid(row=6, column=1, pady=10)

    def plot_graph(self):
        try:
            T0 = float(self.initial_condition_1_entry.get())
            k = float(self.ambient_temp_entry.get())
            Tt = float(self.initial_condition_2_temp_entry.get())
            time = float(self.initial_condition_2_time_entry.get())

            t_values = np.linspace(0, 2*time, 100)
            T_values = k + (T0 - k) * np.exp(-t_values / time)

            fig, ax = plt.subplots()
            ax.plot(t_values, T_values, label='Ley de Enfriamiento de Newton')
            ax.set_xlabel('Tiempo')
            ax.set_ylabel('Temperatura')
            ax.legend()

            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=5, column=1, pady=10)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
    
    def controlarIncognita(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LeyEnfriamientoApp(root)
    root.minsize(700, 300)
    ancho_ventana = 700
    alto_ventana = 300
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x_pos = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    y_pos = int((alto_pantalla / 2) - (alto_ventana / 2))
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
    root.mainloop()
