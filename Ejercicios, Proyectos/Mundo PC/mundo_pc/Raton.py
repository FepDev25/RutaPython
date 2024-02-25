from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones

    @property
    def id_raton(self):
        return self._id_raton

    def __str__(self):
        return f"Raton: [Id: {self._id_raton}, {super().__str__()}]"
