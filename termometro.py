import tkinter as tk
from PIL import Image, ImageTk

class TermometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Termómetro con Slider")

        self.temperatura = tk.DoubleVar()
        self.temperatura.set(0)

        self.slider = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=self.temperatura,
                               label="Temperatura")
        self.slider.pack(pady=20)

        self.termometro_canvas = tk.Canvas(root, width=300, height=400)
        self.termometro_canvas.pack()

        self.actualizar_termometro()

        self.slider.bind("<B1-Motion>", self.actualizar_termometro)

    def actualizar_termometro(self, event=None):
        temperatura = self.temperatura.get()

        color, porcentaje = self.obtener_color_y_porcentaje(temperatura)

        self.termometro_canvas.delete("termometro")

        # Dibujar la barra del termómetro
        self.termometro_canvas.create_rectangle(50, 350, 250, 50, outline="black", width=2)

        # Dibujar la parte coloreada del termómetro
        altura_coloreada = 300 * porcentaje / 100
        self.termometro_canvas.create_rectangle(50, 350, 250, 350 - altura_coloreada, fill=color, outline="black", tags="termometro")

    def obtener_color_y_porcentaje(self, temperatura):
        if 0 <= temperatura <= 59:
            color = "#00FF00"  # Verde
        elif 60 <= temperatura <= 79:
            color = "#FFFF00"  # Amarillo
        elif 80 <= temperatura <= 100:
            color = "#FF0000"  # Rojo

        porcentaje = (temperatura / 100) * 100

        return color, porcentaje

if __name__ == "__main__":
    root = tk.Tk()
    app = TermometroApp(root)
    root.mainloop()
