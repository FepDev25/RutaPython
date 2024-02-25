class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio pio")

    def volar(self, metros):
        print(f"El pajaro a volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "Negro"

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

    @classmethod
    def acceder(cls):
        print(f"Alas: {cls.alas}")

    @staticmethod
    def mirar():
        print("El pajaro mira")

    @staticmethod
    def mirar_dos(objeto):
        print(f"El pajaro mira un {objeto}")





piolin = Pajaro("Amarillo", "Canario")
piolin.volar(6)
Pajaro.poner_huevos(6)
piolin.poner_huevos(5)
piolin.acceder()
piolin.mirar_dos("toro")
