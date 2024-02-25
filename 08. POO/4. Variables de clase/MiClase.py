class MiClase:
    variable_clase = "Valor variable clase"

    def __init__(self, v_instancia):
        self.v_instancia = v_instancia

    @staticmethod
    def metodo_estatico():
         print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.v_instancia)
        print(self.variable_clase)


print(MiClase.variable_clase)
clase1 = MiClase("Chelsea FC")
clase2 = MiClase("Deportivo Cuenca")
print(clase1.v_instancia)
print(clase1.variable_clase)
print(clase2.v_instancia)
print(clase2.variable_clase)

MiClase.variable_clase2 = "Variable Clase 2"
print(MiClase.variable_clase2)
print()
MiClase.metodo_estatico()
MiClase.metodo_clase()
clase2.metodo_estatico()
clase2.metodo_clase()
print()
clase2.metodo_instancia()
