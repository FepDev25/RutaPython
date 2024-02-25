from abc import ABC, abstractmethod

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor invalido: {ancho}")
            self._ancho = 0

        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor invalido: {alto}")
            self._alto = 0

    def __str__(self):
        return f"Figura Geometrica: [Ancho: {self._ancho} Alto: {self._alto}]"

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor invalido: {ancho}")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor invalido: {alto}")

    @abstractmethod
    def calcular_area(self):
        pass

    def _validar_valor(self, valor):
        return True if 0 < valor <= 10 else False
