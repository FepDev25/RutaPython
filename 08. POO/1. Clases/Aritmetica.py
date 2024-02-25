class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar etc 
    """ # DocString para documentar la clase
    
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


print()
aritmetica1 = Aritmetica(5, 3)
print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(round(aritmetica1.dividir(), 2))