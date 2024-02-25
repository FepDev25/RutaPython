from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"

    def calcular_area(self):
        return self.ancho * self.alto

    def hipotenusa_lados(self):
        return round((self.ancho**2 + self.alto**2)**0.5, 2)
