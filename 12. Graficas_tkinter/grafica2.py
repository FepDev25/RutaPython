from tkinter import Tk, Button

def imprimir_mensaje():
    print("Hola, Tkinter!")

ventana = Tk()
boton = Button(ventana, text="Haz clic", command=imprimir_mensaje)
boton.pack()
ventana.mainloop()
