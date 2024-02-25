class Padre:
    def hablar(self):
        print("Hola")


class Madre():
    def hablar(self):
        print("Que tal")

    def reir(self):
        print("Jaja")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


nieto = Nieto()
nieto.hablar()
nieto.reir()
print(Nieto.__mro__)

