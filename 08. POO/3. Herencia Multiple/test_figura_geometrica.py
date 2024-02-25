from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creacion Objetos Cuadrados'.center(50,'-'))
cuadrado1 = Cuadrado(10, "Azul")
print(f"{cuadrado1.__str__()}. Area: {cuadrado1.calcular_area()}")

cuadrado2 = Cuadrado(7, "Rojo")
print(f"{cuadrado2.__str__()}. Area: {cuadrado2.calcular_area()}")

print('Creacion Objetos Rectangulos'.center(50,'-'))

rectangulo1 = Rectangulo(10, 9, "Verde")
rectangulo1.alto = 11
print(f"{rectangulo1.__str__()}. Area: {rectangulo1.calcular_area()}")

rectangulo2 = Rectangulo(6, 2, "Naranja")
print(f"{rectangulo2.__str__()}. Area: {rectangulo2.calcular_area()}")

