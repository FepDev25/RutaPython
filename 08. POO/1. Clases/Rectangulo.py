class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


print()
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
rectangulo1 = Rectangulo(base, altura)
print(f"Area rectangulo: {rectangulo1.calcular_area()}")


base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
rectangulo1 = Rectangulo(base, altura)
print(f"Area rectangulo: {rectangulo1.calcular_area()}")
