from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados

    @property
    def id_teclado(self):
        return self._id_teclado

    def __str__(self):
        return f"Teclado: [Id: {self._id_teclado}, {super().__str__()}]"
