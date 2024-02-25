class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Muuuuuuuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Beeeeee")


vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")


def sonidos_animales(animal):
    animal.hablar()


sonidos_animales(vaca1)
sonidos_animales(oveja1)

