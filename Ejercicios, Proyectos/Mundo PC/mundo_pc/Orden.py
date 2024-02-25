class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_ordenes = Orden.contador_ordenes
        self._computadoras = computadoras

    @property
    def id_ordenes(self):
        return self._id_ordenes

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, comptadoras):
        self._computadoras = comptadoras

    def agregar_computadoras(self, comptadoras):
        self._computadoras.append(comptadoras)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f"Orden {self._id_ordenes}: \n[computadoras: {computadoras_str}]"
