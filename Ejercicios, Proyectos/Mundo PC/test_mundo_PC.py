from mundo_pc.Computadora import Computadora
from mundo_pc.Monitor import Monitor
from mundo_pc.Orden import Orden
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado

raton = Raton("usb", "Sony")
raton2 = Raton("bluetooth", "Acer")
raton3 = Raton("usb", "Samsung")
teclado = Teclado("bluetooth", "HP")
teclado2 = Teclado("bluetooth", "Samsung")
teclado3 = Teclado("usb", "Acer")
monitor = Monitor("Samsung", 7.5)
monitor2 = Monitor("HP", 8)
monitor3 = Monitor("Acer", 7.5)
computadora = Computadora("Gamer", monitor, teclado2, raton2)
computadora2 = Computadora("Entrada usb", monitor2, teclado3, raton)
computadora3 = Computadora("Mixta", monitor3, teclado, raton3)

orden = Orden([computadora])
orden.agregar_computadoras(computadora2)
print(orden)
orden2 = Orden([computadora3])
print(orden2)
orden3 = Orden([computadora2])
orden3.agregar_computadoras(computadora)
orden3.agregar_computadoras(computadora3)
print(orden3)
